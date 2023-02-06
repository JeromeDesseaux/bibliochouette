from threading import local

_user = local()


class CurrentUserMiddleware:
    """
    Middleware which stores request's user into global thread-safe
    variable.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def process_request(self, request):
        _user.value = request.user

    @staticmethod
    def get_current_user():
        if hasattr(_user, "value") and _user.value:
            return _user.value
        return None
