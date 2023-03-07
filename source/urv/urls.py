from django.urls import path
from urv.views.base import index_view

urlpatterns = [
    path("", index_view)
    ]
