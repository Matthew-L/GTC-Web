import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from .guitarstring.guitar_string import GuitarString as GuSt
from .models import StringSet, String


# new calculate
from calculator.stringcalculator.string.length import Length, InvalidStringNumberError
from calculator.stringcalculator.string.guitar_string import GuitarString
from calculator.stringcalculator.scientificpitch.scientific_pitch import ScientificPitch
from calculator.stringcalculator.string_calculator import calculate_tension

ERRORS = []
error = {
    InvalidStringNumberError: 'invalid string number'
}


def get_user_id(username):
    return User.objects.get(username=username).pk


def get_string_set(string_set_name):
    return StringSet.objects.filter(name=string_set_name)


def getUsersStrings(string_set_name, strings, user_set, username):
    for string in strings:
        if username == str(string.string_set.user):
            if str(string.string_set.name) == str(string_set_name):
                # print(string.gauge)
                user_set.append(string)
    return user_set


def getUsersStringSet(context, request):
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
            context['description'] = set.desc
            context['total_strings'] = set.number_of_strings
            user_set = getUsersStrings(string_set_name, strings, user_set, username)
    context['json_string_set'] = serializers.serialize("json", user_set)
    return user_set, context


def load_calculate_page(request):
    context = {}
    if request.method == 'GET':
        try:
            user_set, context = getUsersStringSet(context, request)
        except:
            pass
    return render(request, 'calculate.html', context)


def get_tension(tension_input):
    length = Length(tension_input['scale_length'], tension_input['total_strings'], tension_input['string_number'])
    pitch = ScientificPitch(tension_input['note'], tension_input['octave'])
    string = GuitarString(tension_input['gauge'], tension_input['string_material'])
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


# def user_login_context(context, request):
#     if request.user.is_authenticated():
#         context['is_logged_in'] = True
#         context['username'] = request.user.get_username()
#     else:
#         context['is_logged_in'] = False
#     return context


def return_save_errors(context, errors, request):
    context['errors'] = errors
    return render(request, 'save_set.html', context)


def renaming_set(name, request, user):
    should_rename = False
    try:
        old_name = request.GET['save-set']
        print('changing set name')
        print(name, old_name)
        if name != old_name:
            old_string_set = StringSet.objects.filter(name=old_name, user=user)
            # print(old_string_set, old_name)
            # if old_string_set:
            # old_string_set.all().delete()
            should_rename = True
    except:
        pass

    return old_string_set, should_rename

@csrf_exempt
def asynchronous_save_set(request):
    response = {}
    if request.is_ajax() and request.method == "POST":
        print(request.POST)
        print(request.POST['row[4][note]'])
        print(request.POST['name'])
        # print(request.POST['description'])
        print(request.POST['total_strings'])
        print(request.POST['scale_length'])

        return HttpResponse(json.dumps(response), content_type='application/javascript')


def save_set(request):
    context = {}
    errors = []

    # context = user_login_context(context, request)

    curr = count_string_rows(request)
    if curr == 0:
        errors.append("Nothing Submitted!")
        return return_save_errors(context, errors, request)

    # make new string set
    name = request.GET['string_set_name']
    user = request.user

    desc = request.GET['desc']
    if desc == '':
        desc = ' '
    # check if user is logged in
    if is_anonymous(user):
        errors.append("Register and Log In to Save Sets!")
        return return_save_errors(context, errors, request)

    if is_valid_name(name):
        errors.append("You must give the String Set a name")
        return return_save_errors(context, errors, request)

    # changing set name
    old_string_set = ''
    should_rename = False
    try:
        old_name = request.GET['save-set']
        print('changing set name')
        print(name, old_name)
        if name != old_name:
            old_string_set = StringSet.objects.filter(name=old_name, user=user)
            # print(old_string_set, old_name)
            # if old_string_set:
            # old_string_set.all().delete()
            should_rename = True
    except:
        pass
    # old_string_set, should_rename = renaming_set(name, request, user)
    # check if stringset name exists already

    if renamed_set_exists(should_rename, name, user):
        errors.append("You already have a String Set named that! Delete or rename the set '" + name + "' first.")
        return return_save_errors(context, errors, request)

    # just updating, name stayed the same
    revised_string_set = StringSet.objects.filter(name=name, user=user)
    should_update = False
    if revised_string_set:
        should_update = True

    # verify string parameters
    is_mscale, scale_length, number_of_strings = is_valid_scale_length(context, request, errors)

    if should_update:
        revised_string_set.all().delete()
    elif should_rename:
        old_string_set.all().delete()

    string_set = StringSet(name=name, user=request.user, desc=desc, is_mscale=is_mscale,
                           number_of_strings=number_of_strings)
    try:
        string_set.full_clean()
        string_set.save()
    except ValidationError:
        errors.append("Could not validate String Set input!")
        return return_save_errors(context, errors, request)

    number_of_parameters = 5
    row_errors = 0
    i = 0
    while i < curr:
        # print(i)
        # print(number_of_strings)

        try:
            string_number = request.GET['string_number_GTC_' + str(i)]
            GuSt.sanitize_string_number(string_number)
        except:
            row_errors += 1
            errors.append('Invalid String Number in Row' + str(i))

        try:
            note = request.GET['note_GTC_' + str(i)]
            GuSt.sanitize_note(note)
        except:
            row_errors += 1
            errors.append('Invalid Note in Row' + str(i))

        try:
            octave = request.GET['octave_GTC_' + str(i)]
            GuSt.sanitize_octave(octave)
        except:
            row_errors += 1
            errors.append('Invalid Octave in Row' + str(i))

        try:
            gauge = request.GET['gauge_GTC_' + str(i)]
            GuSt.sanitize_gauge(gauge)
        except:
            row_errors += 1
            errors.append('Invalid Gauge in Row' + str(i))

        try:
            string_type = request.GET['string_type_GTC_' + str(i)]
            GuSt.is_valid_string_material(string_type)
        except:
            row_errors += 1
            errors.append('Invalid String Type in Row' + str(i))
        i += 1

        #print("row_err " + str(row_errors) )
        if row_errors == number_of_parameters:
            while row_errors > 0:
                errors.pop()
                row_errors -= 1
        else:
            row_errors = 0
            string = String(string_set=string_set, string_number=string_number, scale_length=scale_length,
                            note=note, octave=octave, gauge=gauge, string_type=string_type)
            string.save()
            try:
                string.full_clean()
                string_set.save()
            except ValidationError:
                errors.append("Could not validate a guitar string input!")
                return return_save_errors(context, errors, request)

    return return_save_errors(context, errors, request)


def count_string_rows(request):
    curr = 0
    if request.method == 'GET':
        try:
            while request.GET['gauge_GTC_' + str(curr)] is not None:
                print(request.GET['gauge_GTC_' + str(curr)])
                curr += 1
        except KeyError:
            pass

    return curr


def is_anonymous(user):
    if user.is_anonymous():
        return True
    return False


def is_valid_name(name):
    if name == "":
        return True


def is_valid_scale_length(context, request, errors):
    try:
        is_mscale = request.GET["is_mscale"]
        is_mscale = True
    except:
        is_mscale = False

    if is_mscale:
        try:
            scale_length = request.GET['scale_length']
            GuSt.sanitize_multiscale(scale_length)
        except:
            errors.append("Invalid MultiScale Length!")
            return return_save_errors(context, errors, request)
        try:
            number_of_strings = request.GET['number_of_strings']
            GuSt.sanitize_number_of_strings(number_of_strings)
        except:
            errors.append("Invalid Number of Strings!")
            return return_save_errors(context, errors, request)
    else:
        try:
            scale_length = request.GET['scale_length']
            GuSt.sanitize_scale_length(scale_length)
        except:
            errors.append("Invalid Scale Length!")
            return return_save_errors(context, errors, request)
        number_of_strings = 0
    return is_mscale, scale_length, number_of_strings


def renamed_set_exists(should_rename, name, user):
    if should_rename:
        renamed_to_existing_set = StringSet.objects.filter(name=name, user=user)
        if renamed_to_existing_set:
            return True
    return False