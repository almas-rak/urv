from django.urls import path
from urv.views.base import my_view


urlpatterns = [
    path("", my_view)]