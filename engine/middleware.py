import pdb


class RoleAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.role = request.user.role
        else:
            request.role = 'public'

        response = self.get_response(request)
        return response