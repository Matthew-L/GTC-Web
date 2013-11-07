from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.shortcuts import render
from customforms.string import StringForm
from django.template import Context

def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def index(request):
    return render(request, 'index.html')


def calculate(request):
    if request.method == 'POST': # If the form has been submitted...
        form = StringForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = StringForm() # An unbound form

    return render(request, 'calculate.html', {
        'form': form,
    })

def results(request):
    GET_PARAMETERS = ["Note", "String_Type", "Octave", "Gaug e"]
    key = request.GET.keys()
    for parameter in GET_PARAMETERS:
        if parameter not in key:
            return render(request, 'input_error.html')
    is_metric = False
    if "Metric" in key:
        is_metric = True

    #Call Function to calculate tension
    context = Context({'tension':'--tension variable here--'})
    return render(request, 'results.html', context)