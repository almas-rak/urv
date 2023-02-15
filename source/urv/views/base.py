from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.http import require_http_methods
from django.shortcuts import render

from urv.models import Employee


def index_view(request: WSGIRequest):
    Employees = Employee.objects.all()
    context = {
        'Employees': Employees
    }
    return render(request, 'index.html', context=context)



@require_http_methods(["GET", "POST"])
def my_view(request):
    Employees = Employee.objects.all()
    context = {
        'Employees': Employees
    }
    return render(request, context=context)
    
