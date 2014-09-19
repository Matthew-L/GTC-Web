import json

from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.views.generic import View

from .guitarstring.guitar_string import GuitarString as GuSt
from .models import StringSet, String


# new calculate
from calculator.stringcalculator.string.length import Length, InvalidStringNumberError, InvalidScaleLengthError
from calculator.stringcalculator.string.guitar_string import GuitarString
from calculator.stringcalculator.scientificpitch.scientific_pitch import ScientificPitch
from calculator.stringcalculator.string_calculator import calculate_tension

def get_user_id(username):
    return User.objects.get(username=username).pk


def get_string_set(string_set_name):
    return StringSet.objects.filter(name=string_set_name)


def get_users_strings(string_set_name, strings, user_set, username):
    for string in strings:
        if username == str(string.string_set.user):
            if str(string.string_set.name) == str(string_set_name):
                # print(string.gauge)
                user_set.append(string)
    return user_set


def get_users_string_set(context, request):
    user_set = ''
    try:
        username = str(request.GET['users_set'])
        get_user_id(username)
        string_set_name = str(request.GET['string_set_name'])
        string_set = StringSet.objects.filter(name=string_set_name)
        user_set = []
        context['string_set_name'] = string_set_name
        strings = String.objects.all()
        for set in string_set:
            # print('username: ', set.user, username)
            if str(set.user) == str(username):
                context['description'] = set.description
                # context['total_strings'] = set.number_of_strings
                user_set = get_users_strings(string_set_name, strings, user_set, username)
        context['json_string_set'] = serializers.serialize("json", user_set)
    except:
        pass
    return user_set, context


def load_calculate_page(request):
    context = {}
    if request.method == 'GET':
        # try:
        user_set, context = get_users_string_set(context, request)
        # except:
        #     pass
    return render(request, 'calculate.html', context)


def get_tension(tension_input):
    length = Length(tension_input['scale_length'], tension_input['total_strings'], tension_input['string_number'])
    pitch = ScientificPitch(tension_input['note'], tension_input['octave'])
    string = GuitarString(tension_input['gauge'], tension_input['string_type'])
    tension = calculate_tension(length, pitch, string)
    return round_tension(tension)


def round_tension(tension):
    return float("{0:.2f}".format(tension))


@csrf_exempt
def convert_input_to_tension(request):
    """
    Takes a request that contains all the information posted necessary to calculate a strings tension.
    @param request: a request object containing a dictionary of GuSt parameters
    @return: the calculated tension rouned off to 2 decimal places
    """
    response = {}
    tension = 0
    if request.is_ajax() and request.method == "POST":
        print(request.POST)
        try:
            tension = get_tension(request.POST)
        except:
            response['error'] = 'There was an error while processing a string.'
            return HttpResponseBadRequest(json.dumps(response), content_type='application/json')
    response['tension'] = tension
    return HttpResponse(json.dumps(response), content_type='application/javascript')


def return_save_errors(context, errors, request):
    context['errors'] = errors
    return render(request, 'save_set.html', context)

class SaveSet(View):
    response = {}
    errors = []
    valid_strings = []
    user = ''
    old_name = ''
    name = ''
    description = ' '

    def write_strings(self, string_set):
        for s in range(1, len(self.valid_strings) + 1):
            string_inputs = self.valid_strings[s-1]
            string = String(string_set=string_set,
                            string_number=string_inputs['string_number'], 
                            scale_length=string_inputs['scale_length'],
                            note=string_inputs['note'], 
                            octave=string_inputs['octave'], 
                            gauge=string_inputs['gauge'],
                            string_type=string_inputs['string_type'])
            try:
                string.full_clean()
                string.save()
            except ValidationError:
                self.errors.append("Could not validate string " + str(s) + ".")

    def write_set(self):
        string_set = StringSet(name=self.name, user=self.user, description=self.description)
        try:
            string_set.full_clean()
            string_set.save()
            self.write_strings(string_set)
        except ValidationError:
            self.errors.append("Could not validate String Set input!")
        


    def renamed_set_exists(self):
        renamed_to_existing_set = StringSet.objects.filter(name=self.name, user=self.user)
        if renamed_to_existing_set:
            self.errors.append(
                "You already have a String Set named that! Delete or rename the set '" + self.name + "' first.")
            return True
        else:
            return False

    def rename_set(self):
        if not self.renamed_set_exists():
            self.write_set()
            old_string_set = StringSet.objects.filter(name=self.old_name, user=self.user)
            old_string_set.all().delete()

    def revise_set(self):
        revised_set = StringSet.objects.filter(name=self.name, user=self.user)
        if revised_set:
            revised_set.all().delete()
            self.write_set()

    def validate_name(self):
        if self.name == 'Empty' or self.name == '':
            self.errors.append('Name your string set to save it.')
    
    def manage_sets(self):
        if self.name != self.old_name:
            self.rename_set()
        elif self.name == self.old_name:
            self.revise_set()
        else:
            self.write_set()

    def validate_description(self):
        if self.description == '':
            self.description = ' '

    def validate_user_status(self):
        if self.user.is_anonymous():
            self.errors.append("Log in to save sets.")

    def validate_total_strings(self, total):
        if total == '' or total == 0:
            self.errors.append("Add at least one string.")

    def validate_rows(self, request):
        total = int(request.POST['total_strings'])
        for i in range(1, total + 1):
            try:
                tension_input = {
                    'scale_length': request.POST['scale_length'],
                    'total_strings': request.POST['total_strings'],
                    'string_number': i,
                    'note': self.get_row_input(request, i, 'note'),
                    'octave': self.get_row_input(request, i, 'octave'),
                    'gauge': self.get_row_input(request, i, 'gauge'),
                    'string_type': self.get_row_input(request, i, 'string_type')
                }
                get_tension(tension_input)
                self.valid_strings.append(tension_input)
            except InvalidScaleLengthError:
                self.errors.append("An error occurred validating your scale length.")
            except:
                self.errors.append("An error occurred validating string " + str(i))

    @staticmethod
    def get_row_input(request, number, input):
        return request.POST['row[' + str(number) + '][' + input + ']']

    def post(self, request):
        self.errors = []
        self.valid_strings = []
        if request.is_ajax():
            # User Validation
            self.user = request.user
            self.validate_user_status()
            # Description Validation
            try:
                self.description = request.POST['description']
                self.validate_description()
            except MultiValueDictKeyError:
                pass
            # Total Strings Validation
            self.validate_total_strings(request.POST['total_strings'])
            # Validate Rows with Model
            self.validate_rows(request)
            # Name Validation
            self.name = request.POST['name']
            self.old_name = request.POST['old_name']
            self.validate_name()
            if len(self.errors) == 0:
                self.manage_sets()
                # pass
            if len(self.errors) == 0:
                self.response['successMessage'] = 'String set has been saved successfully.'
                return HttpResponse(json.dumps(self.response), content_type='application/javascript')
            elif len(self.errors) != 0:
                self.response['errors'] = self.errors
                return HttpResponseBadRequest(json.dumps(self.response), content_type='application/json')

        # Return Errors
        self.response['errors'] = self.errors
        return HttpResponseBadRequest(json.dumps(self.response), content_type='application/json')

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(SaveSet, self).dispatch(*args, **kwargs)

