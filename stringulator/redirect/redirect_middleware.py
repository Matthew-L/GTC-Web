from django.http import HttpResponsePermanentRedirect

class WWWRedirectMiddleware(object):
    def process_request(self, request):
        if request.META['HTTP_HOST'].startswith('stringulator.herokuapp.com'):
            return HttpResponsePermanentRedirect('http://www.stringulator.com')