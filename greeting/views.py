from django.http import JsonResponse


def greeting(request):
    return JsonResponse({"greeting" : "hello"})


def greeting_new(request):
    return JsonResponse({"greeting": "hello"})