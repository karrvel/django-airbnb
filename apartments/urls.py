from django.urls import path, include
from apartments.views import hello_world, feedback

urlpatterns = [
    # path('hello/<int:user_id>', hello_world),
    path('hello/', hello_world),
    path('feedback/', feedback),
    # path('submit/', submit)
]