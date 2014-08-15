import csv
import json
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from calculator import guitarstring
from calculator.models import StringSet, String


def profile(request):
    context = {}
    context.update(csrf(request))
    if not request.user.is_authenticated():
        return render_to_response('login.html', context, context_instance=RequestContext(request))

    string_sets = StringSet.objects.filter(user=request.user)
    context['string_sets'] = string_sets
    return render_to_response('profile.html', context, context_instance=RequestContext(request))


def downloadStringSet(request):
    # get the response object, this can be used as a stream.
    response = HttpResponse(mimetype='text/csv')
    # force download.
    response['Content-Disposition'] = 'attachment;filename="export.csv"'

    # the csv writer
    writer = csv.writer(response)

    context = {}
    if request.method == 'GET':
        print(request.GET)
        string_set_name = str(request.GET['string_set_name'])
        user = str(request.GET['user'])
        print(user)
        response['Content-Disposition'] = 'attachment;filename="' + string_set_name + ' export.csv"'
        context['string_set_name'] = string_set_name

        string_set = StringSet.objects.filter(name=string_set_name)

        for set in string_set:
            print(set)
            desc = set.desc
            is_mscale = set.is_mscale
            number_of_strings = set.number_of_strings

        strings = String.objects.all()
        user_set = []
        for string in strings:
            if str(string.string_set.name) == str(string_set_name):
                user_set.append(string)

    writer.writerow(["Name", string_set_name])
    writer.writerow(["Description", desc])
    writer.writerow(["Multiscale", is_mscale])
    writer.writerow(["Total Number of Strings", number_of_strings])
    writer.writerow(["Scale Length", string.scale_length])

    writer.writerow(["Number", "Note", "Octave", "Gauge", "String Type", "Tension"])
    for string in user_set:
        if is_mscale:
            gs = guitarstring.GuitarString(string.scale_length, string.string_type, string.gauge, string.note,
                                           string.octave, number_of_strings, string.string_number)
            writer.writerow([string.string_number, string.note, string.octave, string.gauge,
                             string.string_type, gs.calculate_tension()])
        else:
            gs = guitarstring.GuitarString(string.scale_length, string.string_type,
                                           string.gauge, string.note, string.octave)
            writer.writerow([string.string_number, string.note, string.octave, string.gauge, string.string_type,
                             gs.calculate_tension()])

    return response

@csrf_exempt
def ajax_delete_set(request):
    if request.is_ajax() and request.method == "POST":
        name = request.POST['string_set_name']
        user = request.user

        string_set = StringSet.objects.filter(name=name, user=user)
        if string_set:
            string_set.all().delete()
            response = {"name": name}

        return HttpResponse(json.dumps(response), mimetype='application/javascript')

