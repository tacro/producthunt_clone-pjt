from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'product/home.html')

@login_required
def create(request):
    return render(request, 'product/create.html')
