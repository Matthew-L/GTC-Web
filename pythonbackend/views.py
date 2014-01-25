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

    return render(request, 'calculate.html', context)




@csrf_exempt
def ajax(request):
    """
    Takes a request that contains all the information posted necessary to calculate a strings tension.
    @param request: a request object containing a dictionary of GuitarString parameters
    @return: the calculated tension rouned off to 2 decimal places
    """
    if request.is_ajax() and request.method == "POST":
        scale_length = request.POST['scale_length']
        number_of_strings = request.POST['number_of_strings']
        is_mscale = request.POST['is_mscale']
        string_number = request.POST['string_number']
        note = request.POST['note']
        octave = request.POST['octave']
        gauge = request.POST['gauge']
        string_type = request.POST['string_type']
        print(string_number)
        if is_mscale == 'true':
            gs = guitarstring.GuitarString(scale_length, string_type, gauge, note,
                                           octave, number_of_strings, string_number)
        else:
            gs = guitarstring.GuitarString(scale_length, string_type, gauge, note,
                                           octave)
        tension = float("{0:.2f}".format(gs.tension))
        response = {"tension": tension}
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


        print(request.POST["is_mscale"])
        if request.POST["is_mscale"] == 'true':
            print('sl')
            print(request.POST["is_mscale"])
            number_of_strings = request.POST["number_of_strings"]
            gs = guitarstring.GuitarString(scale_length, string_type, gauge, note,
                                       octave, number_of_strings, string_number)
        else:
            gs = guitarstring.GuitarString(scale_length, string_type, gauge, note,
                                       octave)

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
        scale_length = '26.5-30'
        string_number = request.POST['string_number']
        note = 'C'
        octave = 1
        gauge = .001
        string_type = 'PL'
        number_of_strings = request.POST['number_of_strings']
        is_mscale = request.POST['is_mscale']
        response = {"tension": 0}
        print(is_mscale)
        if is_mscale == 'true':
            print(is_mscale)
            gs = guitarstring.GuitarString(scale_length, string_type, gauge, note,
                                       octave, number_of_strings, string_number)
            tension = float("{0:.2f}".format(gs.tension))
            response = {"tension": tension}
        else:
            int(string_number)

        return HttpResponse(json.dumps(response), mimetype='application/javascript')


@csrf_exempt
def isValidNumberOfStrings(request):
    if request.is_ajax() and request.method == "POST":
        scale_length = 32
        string_number = 1
        note = 'C'
        octave = 1
        gauge = .001
        string_type = 'PL'
        number_of_strings = request.POST["number_of_strings"]

        if int(number_of_strings) > 0:
            gs = guitarstring.GuitarString(scale_length, string_type, gauge, note,
                                       octave, number_of_strings, string_number)

            tension = float("{0:.2f}".format(gs.tension))
            response = {"tension": tension}
        return HttpResponse(json.dumps(response), mimetype='application/javascript')
        #except InvalidOctaveError, InvalidGaugeError as e:
        #    print(str(e))

        #print(tension)






def save_set(request):
    context = {}
    errors = []
    if request.user.is_authenticated():
        context['is_logged_in'] = True
        context['username'] = request.user.get_username()
    else:
        context['is_logged_in'] = False
    if request.method == 'GET':
        for user_input in request.GET:
            print(user_input)

        curr = 0
        try:
            while request.GET['gauge_GTC_'+str(curr)] is not None:
                curr += 1
                print(request.GET['gauge_GTC_'+str(curr)])
        except KeyError:
            if curr == 0:
                errors.append("Nothing Submitted! Are you trying to save nothing?!")
                context['errors'] = errors
                return render(request, 'save_set.html', context)

    # make new string set
    name = request.GET['string_set_name']
    user = request.user
    if user.is_anonymous():
        errors.append("Register and Log In to Save Sets!")
        context['errors'] = errors
        return render(request, 'save_set.html', context)

    if StringSet.objects.filter(name=name, user=user):
        print(StringSet.objects.filter(name=name, user=user))
        errors.append("You already used that String Set Name")
        context['errors'] = errors
        return render(request, 'save_set.html', context)

    string_set = StringSet(name=name, user=request.user)
    string_set.save()

    # verify string parameters
    try:
        scale_length = request.GET['scale_length']
        GuitarString.sanitize_scale_length(scale_length)
    except:
        errors.append("Invalid Scale Length!")
        context['errors'] = errors
        return render(request, 'save_set.html', context)

    number_of_strings = curr

    number_of_parameters = 5
    row_errors = 0
    i = 0
    while i < number_of_strings:
        print(i)
        print(number_of_strings)

        try:
            string_number = request.GET['string_number_GTC_'+str(i)]
            print(GuitarString.sanitize_string_numbers(number_of_strings, string_number))

        except:
            row_errors += 1
            errors.append('Invalid String Number in Row' + str(i))

        try:
            note = request.GET['note_GTC_'+str(i)]
            GuitarString(26, 'NW', .009, note, 1, 1, 1)
        except:
            row_errors += 1
            errors.append('Invalid Note in Row' + str(i))

        try:
            octave = request.GET['octave_GTC_'+str(i)]
            GuitarString.sanitize_octave(octave)
        except:
            row_errors += 1
            errors.append('Invalid Octave in Row' + str(i))

        try:
            gauge = request.GET['gauge_GTC_'+str(i)]
            GuitarString.sanitize_gauge(gauge)
        except:
            row_errors += 1
            errors.append('Invalid Gauge in Row' + str(i))

        try:
            string_type = request.GET['string_type_GTC_'+str(i)]
            GuitarString.is_valid_string_material(string_type)
        except:
            row_errors += 1
            errors.append('Invalid String Type in Row' + str(i))
        i += 1

        print("row_err " + str(row_errors) )
        if row_errors == number_of_parameters:
            while row_errors > 0:
                errors.pop()
                row_errors -= 1
        else:
            row_errors = 0
            string = String(string_set=string_set, string_number=string_number, scale_length=scale_length,
                        note=note, octave=octave, gauge=gauge, string_type=string_type)
            string.save()

    context['errors'] = errors

    return render(request, 'save_set.html', context)

def deleteSet(request):
    context = {}
    errors = []
    name = request.GET['string_set_name']
    user = request.user
    string_set = StringSet.objects.filter(name=name, user=user)
    if string_set:
        print(StringSet.objects.filter(name=name, user=user))
        # errors.append("You already used that String Set Name")
        # context['errors'] = errors
        string_set.all().delete()

    else:
        errors.append( 'You do not have '+str(string_set)+'in your profile.')
    return render(request, 'delete_set.html', context)

@csrf_exempt
def ajaxDeleteSet(request):
    if request.is_ajax() and request.method == "POST":
        name = request.POST['string_set_name']
        user = request.user
        print(name)

        string_set = StringSet.objects.filter(name=name, user=user)
        if string_set:
            print(StringSet.objects.filter(name=name, user=user))
            # errors.append("You already used that String Set Name")
            # context['errors'] = errors
            string_set.all().delete()
            response = {"name": name}

        return HttpResponse(json.dumps(response), mimetype='application/javascript')

