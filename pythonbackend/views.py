from django.shortcuts import render
from customforms.string import StringForm, SubmitStringForm
from calculator.guitarstring import GuitarString
from pythonbackend.models import StringSet, String
import ast
from django.core.context_processors import csrf


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
    context.update(csrf(request))
    return render(request, 'calculate.html', context)





def save_string(request):
    print(request.POST)
    context = {}
    if request.user.is_authenticated():
        context['is_logged_in'] = True
        context['username'] = request.user.get_username()
        username = request.user.get_username()
        scale_length = ast.literal_eval(request.POST["Scale_Length"])
        string_material = request.POST["String_Type"]
        gauge = ast.literal_eval(request.POST["Gauge"])
        note = request.POST["Note"]
        octave = ast.literal_eval(request.POST["Octave"])
        #user_string = strings(username=username, scale_length=scale_length, note=note, octave=octave, gauge=gauge, string_type=string_material)
        #user_string.save()



    return render(request, 'save_string.html')






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
    POST_PARAMETERS = ["String_Type", "Octave", "Gauge", "Scale_Length"]
    key = request.POST.keys()
    print(key)
    for parameter in POST_PARAMETERS:
        print(parameter)
        if parameter not in key:
            return render(request, 'input_error.html')

    if is_valid_result(request.POST):
        scale_length = ast.literal_eval(request.POST["Scale_Length"])
        string_material = request.POST["String_Type"]
        gauge = ast.literal_eval(request.POST["Gauge"])
        note = request.POST["Note"]
        octave = ast.literal_eval(request.POST["Octave"])
        guitar_string = GuitarString(scale_length, string_material, gauge, note, octave)
        guitar_string.tension = float("{0:.2f}".format(guitar_string.tension))
        context['string_list'] = [guitar_string]
        initdata = {}
        initdata['Username'] = request.user.get_username()
        initdata['Scale_Length'] = scale_length
        initdata['Note'] = note
        initdata['Octave'] = octave
        initdata['Gauge'] = gauge
        initdata['String_Type'] = string_material
        print(initdata)
        context.update(csrf(request))
        form = SubmitStringForm(initial=initdata)
        context['form'] = form
        return render(request, 'results.html', context)

    return render(request, 'input_error.html', context)




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
