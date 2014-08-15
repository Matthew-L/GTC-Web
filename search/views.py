from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from calculator.models import StringSet


def search(request):
    context = {}
    context.update(csrf(request))
    print('search')
    # context = {}
    if request.user.is_authenticated():
        context['is_logged_in'] = True
        context['username'] = request.user.get_username()
    else:
        context['is_logged_in'] = False
    errors = []
    if 'query' in request.GET:
        query = request.GET['query']
        if not query:
            errors.append('Enter a search term.')
        elif len(query) > 50:
            errors.append('Please enter at most 50 characters.')
        else:
            context['search_name_results'] = StringSet.objects.filter(name__icontains=query)
            context['search_desc_results'] = StringSet.objects.filter(desc__icontains=query)
        context['errors'] = errors
    print(request)
    return render_to_response('search-results.html', context, context_instance=RequestContext(request))
    # return render(request, 'search_results.html', context)