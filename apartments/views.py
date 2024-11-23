from django.shortcuts import render
from django import http
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
# def hello_world(request: HttpRequest) -> HttpResponse:
#     if request.method == "GET":
#         return HttpResponse("<b>hello world</b>")
#     if request.method == "POST":
#         return HttpResponse(f"{datetime.now()}")


class HelloWorld(View):
    def get(self, request):
        return HttpResponse("<b>hello world</b>")
    
    @csrf_exempt
    def post(self, request):
         return HttpResponse(f"{datetime.now()}")
