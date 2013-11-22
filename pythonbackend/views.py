from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from calculator import guitarstring
from customforms.string import StringForm, SubmitStringForm
from calculator.guitarstring import GuitarString, InvalidOctaveError, InvalidGaugeError
from pythonbackend.models import StringSet, String
import ast
from django.core.context_processors import csrf
from pythonbackend.models import StringSetForm, StringForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.core import serializers
import json

MAX_STRINGS = 12


def edit_set(request):
    context = {}
    if request.method == 'GET':
        print("using 'GET'")
        string_set_name = 'First Set'#str(request.GET['string_set_name'])
        print("String set name: " + string_set_name)
        context['string_set_name'] = string_set_name
        strings = String.objects.all()
        user_set = []
        for string in strings:
            if str(string.string_set.name) == str(string_set_name):
                user_set.append(string)
    data = serializers.serialize("json", user_set)
    print(data)
    context['json_data'] = data
    context['someDjangoVariable'] = data
    context['MAX_STRINGS'] = MAX_STRINGS
    return render(request, 'edit_string_set.html', context)


"""
Sends the form that gets the user input for the strings
"""


def calculate(request):
    if request.method == 'POST':
        string_form = StringForm(request.POST)
        set_form = StringSetForm(request.POST)
        if set_form.is_valid():
            set_form.save()
            return HttpResponseRedirect('/')

        if string_form.is_valid():
            string_form.save()
            return HttpResponseRedirect('/')



    context = {}
    if request.user.is_authenticated():
        context['is_logged_in'] = True
        context['username'] = request.user.get_username()
    else:
        context['is_logged_in'] = False

    context['string_set_form'] = StringSetForm(initial={'user': request.user.id})

    form = StringForm(user=request.user)
    context['form'] = form
    context['MAX_STRINGS'] = MAX_STRINGS
    context.update(csrf(request))

    return render(request, 'calculate.html', context)





VALIDATE_PARAMETERS = ["String_Type", "Octave", "Gauge", "Scale_Length"]
ACCEPTED_NOTES = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']
OCTAVE_RANGE = 11
STRING_TYPE = ["PL", "PB", "NW", "XS", "HR"]




"""
    Checks that users input is valid
    result = Dictionary of data to be sent to GuitarString
    return boolean if result is valid
"""
def is_valid_result(result):
    print("In is_valid_result")
    for parameter in VALIDATE_PARAMETERS:
        if parameter not in result.keys():
            return False

    if result['String_Type'] not in STRING_TYPE:
        return False

    gauge = result['Gauge']
    if gauge.count('.') < 2:
        temp_gauge = gauge.replace('.', '')
        if temp_gauge.isdigit():
            if float(gauge) < 0:
                return False
        else:
            return False


    if result['Note'] not in ACCEPTED_NOTES:
        return False

    scale_length = result['Scale_Length']
    if scale_length.count('.') < 2:
        temp_scale_length = scale_length.replace('.', '')
        if temp_scale_length.isdigit():
            if float(scale_length) < 0:
                return False
        else:
            return False

    return True



@csrf_exempt
def ajax(request):
    if request.is_ajax() and request.method == "POST":
        string_set_name = request.POST['string_set_name']
        scale_length = request.POST['scale_length']
        string_number = request.POST['string_number']
        note = request.POST['note']
        octave = request.POST['octave']
        gauge = request.POST['gauge']
        string_type = request.POST['string_type']
        number_of_strings = request.POST['string_type']

        #try:
        gs = guitarstring.GuitarString(scale_length, string_type, gauge, note,
                                           octave, number_of_strings, string_number)
        tension = float("{0:.2f}".format(gs.tension))
        response = {"tension": tension}
        #except InvalidOctaveError, InvalidGaugeError as e:
        #    print(str(e))

        print(tension)

        return HttpResponse(json.dumps(response), mimetype='application/javascript')
