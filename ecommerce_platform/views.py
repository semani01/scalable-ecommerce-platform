from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Welcome to the Scalable E-Commerce Platform API!"})
