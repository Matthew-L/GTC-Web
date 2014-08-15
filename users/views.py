from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def login(request):
    context = {}
    context.update(csrf(request))
    return render_to_response('login.html', context, context_instance=RequestContext(request))

def auth_view(request):
    username = request.POST.get('username', '')
    print(username)
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/profile/')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def invalid_login(request):
    return render(request, 'invalid_login.html')
    # return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)
    return redirect('stringulator.views.load_homepage')

def register_user(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stringulator.views.load_homepage')
            # return HttpResponseRedirect('/accounts/register_success')

    context = {}
    context.update(csrf(request))
    context['form'] = UserCreationForm()
    return render_to_response('register.html', context, context_instance=RequestContext(request))


def register_success(request):
    context = {}
    return render_to_response('register_success.html', context)




