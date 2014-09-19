import csv
import json
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from calculator import guitarstring
from calculator.models import StringSet, String
from calculator.views import get_tension


def profile(request):
    context = {}
    context.update(csrf(request))
    if not request.user.is_authenticated():
        return render_to_response('login.html', context, context_instance=RequestContext(request))

    string_sets = StringSet.objects.filter(user=request.user)
    context['string_sets'] = string_sets
    return render_to_response('profile.html', context, context_instance=RequestContext(request))


def convert_to_tension_input(string):
    tension_input = {}
    print(str(string.string_number))
    tension_input['string_number'] = string.string_number
    tension_input['note'] = string.note
    tension_input['octave'] = string.octave
    tension_input['gauge'] = string.gauge
    tension_input['string_type'] = string.string_type
    return tension_input
    # tension_input['scale_length'] = string.
    # length = Length(tension_input['scale_length'], tension_input['total_strings'], tension_input['string_number'])
    # pitch = ScientificPitch(tension_input['note'], tension_input['octave'])
    # string = GuitarString(tension_input['gauge'], tension_input['string_type'])


def downloadStringSet(request):
    # get the response object, this can be used as a stream.
    response = HttpResponse(mimetype='text/csv')
    # force download.
    response['Content-Disposition'] = 'attachment;filename="export.csv"'
    # the csv writer
    writer = csv.writer(response)
    context = {}
    if request.method == 'GET':
        string_set_name = str(request.GET['string_set_name'])
        response['Content-Disposition'] = 'attachment;filename="' + string_set_name + ' export.csv"'
        context['string_set_name'] = string_set_name
        user = str(request.GET['user'])
        user = User.objects.filter(username=user)
        string_set = StringSet.objects.filter(name=string_set_name, user=user)
        description = ''
        for set in string_set:
            print(set)
            description = set.description
            number_of_strings = 8

        strings = String.objects.all()
        user_set = []
        total_strings = 0
        for string in strings:
            if str(string.string_set.name) == str(string_set_name):
                if string.string_number > total_strings:
                    total_strings = string.string_number
                user_set.append(string)
        scale_length = user_set[0].scale_length
        writer.writerow(["Name", string_set_name])
        writer.writerow(["Description", description])
        writer.writerow(["Scale Length", scale_length])

        writer.writerow(["Number", "Note", "Octave", "Gauge", "String Type", "Tension"])

        for string in user_set:

            tension_input = convert_to_tension_input(string)
            tension_input['total_strings'] = total_strings
            tension_input['scale_length'] = scale_length
            tension = get_tension(tension_input)
            # get_tension(tension_input)
            # gs = guitarstring.GuitarString(string.scale_length, string.string_type,
            # string.gauge, string.note, string.octave)
            writer.writerow([string.string_number, string.note, string.octave, string.gauge, string.string_type,
                             tension])

    return response


@csrf_exempt
def delete_set(request):
    if request.is_ajax() and request.method == "POST":
        response = {}
        errors = []

        name = request.POST['setName']
        user = request.user

        string_set = StringSet.objects.filter(name=name, user=user)
        if str(request.user) == str(user):
            if string_set:
                string_set.all().delete()
                response = {"name": name}
                return HttpResponse(json.dumps(response), content_type='application/javascript')
            else:
                errors.append("The string set does not exist anymore.")
        else:
            errors.append("You can only delete your own strings.")
        response['errors'] = errors
        return HttpResponseBadRequest(json.dumps(response), content_type='application/json')

