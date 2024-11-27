from django.shortcuts import render
from django import http
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

from apartments.models import Apartment


@csrf_exempt
def hello_world(request: HttpRequest, user_id) -> HttpResponse:
    if request.method == "GET":
        # return HttpResponse(f"<h1>hello {username}</h1>")

        apartments = Apartment.objects.filter(owner__id=user_id)
        
        print(apartments)

        context = {
            'apartments': apartments
        }
        return render(request, 'hello_world.html', context=context)
    if request.method == "POST":
        return HttpResponse(f"{datetime.now()}")


# class HelloWorld(View):
#     def get(self, request):
#         return HttpResponse("<b>hello world</b>")
    
#     @csrf_exempt
#     def post(self, request):
#          return HttpResponse(f"{datetime.now()}")
