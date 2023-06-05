import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views import View

from oauth2_provider.decorators import protected_resource

from .oauth import oauth


@require_http_methods(["POST"])
@protected_resource(scopes=['user_id'])
def greeting_func():
    if request.method == "POST":
        json_data = json.loads(request.body)
        value = json_data.get("greeting", None)
        if value == "hello":
            return JsonResponse({"greeting": "hello to you too"})
        else:
            return JsonResponse({"greeting": f"{value} to you too"})


class Greeting(View):

    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        value = json_data.get("greeting", None)
        if value == "hello":
            return JsonResponse({"greeting": "hello to you too"})
        else:
            return JsonResponse({"greeting": f"{value} to you too"})


def login(request):
    # build a full authorize callback uri
    redirect_uri = request.build_absolute_uri('/authorize/')
    return oauth.lms.authorize_redirect(request, redirect_uri)


def authorize(request):
    # This will create a http request client that points to the LMS.
    lms = oauth.create_client('lms')
    # Here, we authenticate the client with the token we got from the LMS. In a real-world
    # application, we'd save this token somehow for subsequent requests.
    token = lms.authorize_access_token(request)
    # And then, we use this token to fetch the user's info.
    resp = lms.get('/api/user/v1/me', token=token)
    resp.raise_for_status()
    profile = resp.json()
    # Now that we have the user's info, we can render a page with the relevant info.
    return render(request, 'authorize.html', {'profile': profile})