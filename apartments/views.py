from django.shortcuts import render
from django import http
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

from apartments.models import Apartment
from apartments.forms import FeedbackForm, ApartmentForm

# def submit(request):
#     # print(request.GET.get('name'))
#     # print(request.GET.get('email'))
#     # return HttpResponse(request.GET.get('name'))

#     form = FeedbackForm(request)
#     print(dict(form))
#     return HttpResponse(form)



def feedback(request):
    if request.method == "POST":
        # form = FeedbackForm(request.POST)
        form = ApartmentForm(request.POST)
        # print(form)
        # print(dict(form.cleaned_data))

        if form.is_valid():
            print(form)
            print(form.cleaned_data)
            apartment = form.save(commit=False)
            apartment.save()
            print(apartment)
        else:
            print(form.errors)
            return HttpResponse(f"{form.errors}")


        return HttpResponse("Submitted!")

    if request.method == "GET":
        # form = FeedbackForm()
        form = ApartmentForm()
        return render(request, 'feedback.html', {'ismoil': form})


@csrf_exempt
# def hello_world(request: HttpRequest, user_id) -> HttpResponse:
def hello_world(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        # return HttpResponse(f"<h1>hello {username}</h1>")

        # exact, iexact, icontains, lt, lte, gt, gte, range
        # apartments = Apartment.objects.filter(daily_price__range=(6, 100))
        # apartments = Apartment.objects.exclude(daily_price__lt=5)
        apartments = Apartment.objects.all().order_by('daily_price', '-name')
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
