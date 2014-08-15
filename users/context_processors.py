
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