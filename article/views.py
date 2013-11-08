from django.http import HttpResponse


def hello(request):
    name = "matt"
    html = "<html><body>Hi %s, this worked!</body></html>" % name
    return HttpResponse(html)
