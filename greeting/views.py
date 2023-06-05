import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views import View

from oauth2_provider.decorators import protected_resource


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