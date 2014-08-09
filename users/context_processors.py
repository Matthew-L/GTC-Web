# def authenticate_user(request):
#     context = {}
#     context = set_is_logged_in(request, context)
#     context = set_session_username(request, context)
#     return context
#
#
# # Login
#
# def set_is_logged_in(context):
#     is_logged_in = request.user.is_authenticated()
#     context['is_logged_in'] = is_logged_in
#     return context
#
#
# def set_session_username(request, context):
#     if request.user.is_authenticated():
#         context['username'] = request.user.get_username()
#     return context


from django import template
from django.contrib.auth.forms import AuthenticationForm

# register = template.Library()

# @register.inclusion_tag('registration/login.html', takes_context=True)
def login(context):
    """
    the login form
    {% load login %}{% login %}
    """
    request = context.get('request', None)
    if not request:
        return

    dict(is_logged_in=request.user.is_authenticated())
    return dict(username=request.user.get_username())