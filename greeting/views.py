from django.http import JsonResponse
from djago.views import View


class Greeting(View):

    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        value = json_data.get("greeting", None)
        if value == "hello":
            return JsonResponse({"greeting": "hello to you too"})
        else:
            return JsonResponse({"greeting": f"{value} to you too"})