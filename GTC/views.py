from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.shortcuts import render
from customforms.contact import StringForm

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