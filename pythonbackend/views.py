from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from calculator import guitarstring
from calculator.guitarstring import GuitarString
from pythonbackend.models import StringSet, String
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
import json
from django.core.exceptions import ValidationError

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

        try:
            string_set_name = str(request.GET['string_set_name'])
            string_set = StringSet.objects.filter(name=string_set_name)

            #print(context['fields']['scale_length'])
        except:
            return render(request, 'calculate.html', context)

        user_set = []
        # wont iterate any other way for some reason
        for set in string_set:
            #user_set.append(set)
            #user_set.append(set.desc)
            #user_set.append(set.number_of_strings)
            context['is_mscale'] = set.is_mscale
            context['desc'] = set.desc
            context['number_of_strings'] = set.number_of_strings

        context['string_set_name'] = string_set_name


        strings = String.objects.all()

        for string in strings:
            if str(string.string_set.name) == str(string_set_name):
                user_set.append(string)
        data = serializers.serialize("json", user_set)
        #print(data)
        context['json_data'] = data
        context['someDjangoVariable'] = data

    return render(request, 'calculate.html', context)




@csrf_exempt
def ajax_calculate(request):
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





def save_set(request):
    context = {}
    errors = []

    if request.user.is_authenticated():
        context['is_logged_in'] = True
        context['username'] = request.user.get_username()
    else:
        context['is_logged_in'] = False
    if request.method == 'GET':
        #for user_input in request.GET:
        #    print(user_input)
        curr = 0
        try:
            while request.GET['gauge_GTC_'+str(curr)] is not None:
                print(request.GET['gauge_GTC_'+str(curr)])
                curr += 1
        except KeyError:
            if curr == 0:
                errors.append("Nothing Submitted! Are you trying to save nothing?!")
                context['errors'] = errors
                return render(request, 'save_set.html', context)

    # make new string set
    name = request.GET['string_set_name']
    user = request.user
    desc = request.GET['desc']
    if desc == '':
        desc = ' '
    #check if user is logged in
    if user.is_anonymous():
        errors.append("Register and Log In to Save Sets!")
        context['errors'] = errors
        return render(request, 'save_set.html', context)
    if name == "":
        errors.append("You must give the String Set a name")
        context['errors'] = errors
        return render(request, 'save_set.html', context)


    #changing set name
    try:
        should_rename = False
        old_name = request.GET['save-set']
        if name != old_name:
            old_string_set = StringSet.objects.filter(name=old_name, user=user)
            # print(old_string_set, old_name)
            # if old_string_set:
                # old_string_set.all().delete()
            should_rename = True
    except:
        pass

    #check if stringset name exists already
    if should_rename:
        renamed_to_existing_set = StringSet.objects.filter(name=name, user=user)
        if renamed_to_existing_set:
            errors.append("You already have a String Set named that! Delete or rename the set '"+name+"' first.")
            context['errors'] = errors
            return render(request, 'save_set.html', context)

    #just updating, name stayed the same
    revised_string_set = StringSet.objects.filter(name=name, user=user)
    should_update = False
    if revised_string_set:
        should_update = True

    # verify string parameters
    try:
        is_mscale = request.GET["is_mscale"]
        is_mscale = True
    except:
        is_mscale = False

    if is_mscale:
        try:
            scale_length = request.GET['scale_length']
            GuitarString.sanitize_multiscale(scale_length)
        except:
            errors.append("Invalid MultiScale Length!")
            context['errors'] = errors
            return render(request, 'save_set.html', context)
        try:
            number_of_strings = request.GET['number_of_strings']
            GuitarString.sanitize_number_of_strings(number_of_strings)
        except:
            errors.append("Invalid Number of Strings!")
            context['errors'] = errors
            return render(request, 'save_set.html', context)
    else:
        try:
            scale_length = request.GET['scale_length']
            GuitarString.sanitize_scale_length(scale_length)
        except:
            errors.append("Invalid Scale Length!")
            context['errors'] = errors
            return render(request, 'save_set.html', context)
        number_of_strings = 0

    if should_update:
        revised_string_set.all().delete()
    elif should_rename:
        old_string_set.all().delete()

    string_set = StringSet(name=name, user=request.user, desc=desc, is_mscale=is_mscale, number_of_strings=number_of_strings)
    try:
        string_set.full_clean()
        string_set.save()
    except ValidationError:
        errors.append("Could not validate String Set input!")
        context['errors'] = errors
        return render(request, 'save_set.html', context)

    number_of_parameters = 5
    row_errors = 0
    i = 0
    while i < curr:
        # print(i)
        # print(number_of_strings)

        try:
            string_number = request.GET['string_number_GTC_'+str(i)]
            GuitarString.sanitize_string_number(string_number)
        except:
            row_errors += 1
            errors.append('Invalid String Number in Row' + str(i))

        try:
            note = request.GET['note_GTC_'+str(i)]
            GuitarString.sanitize_note(note)
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
                context['errors'] = errors
                return render(request, 'save_set.html', context)

    context['errors'] = errors

    return render(request, 'save_set.html', context)

def edit_set(request):
    pass


@csrf_exempt
def ajax_delete_set(request):
    if request.is_ajax() and request.method == "POST":
        name = request.POST['string_set_name']
        user = request.user
        # print(name)

        string_set = StringSet.objects.filter(name=name, user=user)
        if string_set:
            # print(StringSet.objects.filter(name=name, user=user))
            # errors.append("You already used that String Set Name")
            # context['errors'] = errors
            string_set.all().delete()
            response = {"name": name}

        return HttpResponse(json.dumps(response), mimetype='application/javascript')


