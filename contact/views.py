from django.shortcuts import render
from users.views import authenticate_user


def load_contact_page(request):
    context = authenticate_user(request, {})
    return render(request, 'contact.html', context)

def load_test_page(request):
    context = authenticate_user(request, {})
    return render(request, 'index-test.html', context)

def load_base_bak_page(request):
    context = authenticate_user(request, {})
    return render(request, 'base-bak.html', context)