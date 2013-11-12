from django.shortcuts import render
from customforms.string import StringForm
from calculator.calculate import GTC
import ast



"""
Sends the form that gets the user input for the strings
"""
def calculate(request):
    context = {}
    if request.user.is_authenticated():
        context['is_logged_in'] = True
        context['username'] = request.user.get_username()
    else:
        context['is_logged_in'] = False
    form = StringForm()
    context['form'] = form
    return render(request, 'calculate.html', context)





"""
Generates the view that displays the tension or an error page there is an error in the input
"""
def results(request):
    context = {}
    if request.user.is_authenticated():
        context['is_logged_in'] = True
        context['username'] = request.user.get_username()
    else:
        context['is_logged_in'] = False
    GET_PARAMETERS = ["String_Type", "Octave", "Gauge", "Scale_Length"]
    key = request.GET.keys()
    print(key)
    for parameter in GET_PARAMETERS:
        print(parameter)
        if parameter not in key:
            return render(request, 'input_error.html')

    if is_valid_result(request.GET):
        scale_length = ast.literal_eval(request.GET["Scale_Length"])
        string_material = request.GET["String_Type"]
        gauge = ast.literal_eval(request.GET["Gauge"])
        note = request.GET["Note"]
        octave = ast.literal_eval(request.GET["Octave"])
        guitar_string = GTC(scale_length, string_material, gauge, note, octave)
        context['string_list'] = [guitar_string]
        return render(request, 'results.html', context)

    return render(request, 'input_error.html', context)




VALIDATE_PARAMETERS = ["String_Type", "Octave", "Gauge", "Scale_Length"]
ACCEPTED_NOTES = ['A', 'C', 'C#/Db', 'D', 'Eb/D#', 'E', 'F', 'F#/Gb', 'G', 'Ab/G#']
OCTAVE_RANGE = 11
STRING_TYPE = ["PL", "PB", "NW", "XS", "HR"]




"""
    Checks that users input is valid
    result = Dictionary of data to be sent to GTC
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
    if gauge.count('.')  < 2:
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
