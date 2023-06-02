from django.http import JsonResponse


def greeting(request):
    return JsonResponse({"greeting" : "hello"})
    # if request.data == "hello":
    # 	pass
    # else:
    # 	return JsonResponse({"greeting" : "hello"})
    # return JsonResponse(data)