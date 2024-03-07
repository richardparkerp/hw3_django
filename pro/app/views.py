from django.shortcuts import render
from .models import *

def all_list(request):
    all = Card.objects.all()
    return render(request,'home.html',{'cards':all})


