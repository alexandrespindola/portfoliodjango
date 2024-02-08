from django.shortcuts import render
from .models import Case

def index(request):
    cases = Case.objects.all()
    return render(request, 'app/index.html', {'cases': cases})

# from django.shortcuts import render

# def index(request):
#     return render(request, 'app/index.html')