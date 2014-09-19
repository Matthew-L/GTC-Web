from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# def login(request):
#     context = {}
#     context.update(csrf(request))
#     return render_to_response('login.html', context, context_instance=RequestContext(request))

def login(request):
    username = request.POST.get('username', '')
    print(username)
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/profile/')
    else:
        return HttpResponseRedirect('/invalid-login')


def invalid_login(request):
    return render(request, 'invalid_login.html')
    # return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)
    return redirect('stringulator.views.load_homepage')

def register_user(request):
    error = 'No data received. Make sure to fill out the all forms to register.'
    if request.method == 'POST':
        user = User.objects.filter(username=request.POST['username'])
        if user:
            error = 'The username is taken.'
        elif request.POST['password1'] != request.POST['password2']:
            error = 'Your password did not match.'
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            auth.login(request, new_user)
            return redirect('stringulator.views.load_homepage')
            # return HttpResponseRedirect('/accounts/register_success')

        context = {}
        context['error'] = error
        context.update(csrf(request))
        # context['form'] = UserCreationForm()
        # return render_to_response('invalid_login.html', context, context_instance=RequestContext(request))
        return render(request, 'invalid_login.html', context)


# def register_success(request):
#     context = {}
#     return render_to_response('register_success.html', context)




