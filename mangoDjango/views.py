from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from pythonbackend.models import StringSet, String


def set_users_login_status(request):
    context = {}
    if request.user.is_authenticated():
        context['is_logged_in'] = True
        context['username'] = request.user.get_username()
    else:
        context['is_logged_in'] = False
    return context


def login(request):
    context = set_users_login_status(request)
    context.update(csrf(request))
    return render_to_response('login.html', context)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/profile/')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def invalid_login(request):
    return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

####################################
def register_user(request):
    context = set_users_login_status(request)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    context.update(csrf(request))

    context['form'] = UserCreationForm()
    return render_to_response('register.html', context)


def register_success(request):
    context = set_users_login_status(request)
    return render_to_response('register_success.html', context)


def profile(request):
    context = set_users_login_status(request)
    context.update(csrf(request))
    if not context['is_logged_in']:
        return render_to_response('login.html', context)

    string_sets = StringSet.objects.filter(user=request.user)
    context['string_sets'] = string_sets
    return render_to_response('profile.html', context)

def search(request):
    context = {}
    if request.method == 'GET':
        print('here ' + str(request.GET['query']))
        if 'query' in request.GET:
            context['search_result'] = 'You searched for: %r' % request.GET['query']
        else:
            context['search_result'] = 'You submitted an empty form.'
        print(context['search_result'])
    return HttpResponse('search_result', context)