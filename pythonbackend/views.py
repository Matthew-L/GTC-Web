from django.shortcuts import render
from customforms.string import StringForm, SubmitStringForm
from calculator.guitarstring import GuitarString
from pythonbackend.models import StringSet, String
import ast
from django.core.context_processors import csrf
from pythonbackend.models import StringSetForm, StringForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


"""
Sends the form that gets the user input for the strings
"""
MAX_STRINGS = 12


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
