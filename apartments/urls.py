from django.urls import path, include
from apartments.views import hello_world

urlpatterns = [
    path('hello/<int:user_id>', hello_world)
]