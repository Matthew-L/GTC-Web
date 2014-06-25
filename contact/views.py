from django.shortcuts import render
from users.views import authenticate_user


def load_contact_page(request):
    context = authenticate_user(request)
    return render(request, 'contact.html', context)
