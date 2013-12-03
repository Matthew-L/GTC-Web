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


def calculate(request):
    context = {}
    try:
        if request.user.is_authenticated():
            context['is_logged_in'] = True
            context['username'] = request.user.get_username()
        else:
            context['is_logged_in'] = False
    except:
        HttpResponseRedirect('/accounts/login')

    if request.method == 'GET':
        print("using 'GET'")
        try:
            string_set_name = str(request.GET['string_set_name'])
        except:
            return render(request, 'calculate.html', context)

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
    return render(request, 'calculate.html', context)


"""
Sends the form that gets the user input for the strings
"""
#
#VALIDATE_PARAMETERS = ["String_Type", "Octave", "Gauge", "Scale_Length"]
#ACCEPTED_NOTES = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']
#OCTAVE_RANGE = 11
#STRING_TYPE = ["PL", "PB", "NW", "XS", "HR"]
#
#


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
    """
    Takes a request that contains all the information posted necessary to calculate a strings tension.
    @param request: a request object containing a dictionary of GuitarString parameters
    @return: the calculated tension rouned off to 2 decimal places
    """
    if request.is_ajax() and request.method == "POST":
        #string_set_name = request.POST['string_set_name']
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

@csrf_exempt
def isValidScaleLength(request):
    if request.is_ajax() and request.method == "POST":

        scale_length = request.POST['scale_length']
        string_number = 1
        note = 'C'
        octave = 1
        gauge = .001
        string_type = 'PL'
        number_of_strings = 1

        #try:
        gs = guitarstring.GuitarString(scale_length, string_type, gauge, note,
                                       octave, number_of_strings, string_number)
        tension = float("{0:.2f}".format(gs.tension))
        response = {"tension": tension}
        #except InvalidOctaveError, InvalidGaugeError as e:
        #    print(str(e))

        print(tension)

        return HttpResponse(json.dumps(response), mimetype='application/javascript')


@csrf_exempt
def isValidGauge(request):
    if request.is_ajax() and request.method == "POST":
        scale_length = 32
        string_number = 1
        note = 'C'
        octave = 1
        gauge = request.POST['gauge']
        string_type = 'PL'
        number_of_strings = 1

        #try:
        gs = guitarstring.GuitarString(scale_length, string_type, gauge, note,
                                       octave, number_of_strings, string_number)
        tension = float("{0:.2f}".format(gs.tension))
        response = {"tension": tension}
        #except InvalidOctaveError, InvalidGaugeError as e:
        #    print(str(e))

        print(tension)

        return HttpResponse(json.dumps(response), mimetype='application/javascript')


@csrf_exempt
def isValidStringNumber(request):
    if request.is_ajax() and request.method == "POST":
        scale_length = 32
        string_number = request.POST['string_number']
        note = 'C'
        octave = 1
        gauge = .001
        string_type = 'PL'
        number_of_strings = 1

        #try:
        gs = guitarstring.GuitarString(scale_length, string_type, gauge, note,
                                       octave, number_of_strings, string_number)
        tension = float("{0:.2f}".format(gs.tension))
        response = {"tension": tension}
        #except InvalidOctaveError, InvalidGaugeError as e:
        #    print(str(e))

        print(tension)

        return HttpResponse(json.dumps(response), mimetype='application/javascript')


#@csrf_exempt
def save_set(request):
     #if request.is_ajax() and request.method == "POST":
     #   #string_set_name = request.POST['string_set_name']
     #   scale_length = request.POST['scale_length']
     #
     #
     #   string_number = request.POST['string_number']
     #   note = request.POST['note']
     #   octave = request.POST['octave']
     #   gauge = request.POST['gauge']
     #   string_type = request.POST['string_type']
     #   number_of_strings = request.POST['string_type']
    print('here')
    if request.method == 'GET':
        #context.update(csrf(request))
        for user_input in request.GET:
            print(user_input)


    print(request.GET['string_set_name'])
    return render(request, 'save_set.html')