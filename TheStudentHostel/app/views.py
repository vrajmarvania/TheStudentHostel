from urllib import request

from django.shortcuts import render

def index(request):

    return render(request,'app/index.html')
def search(request):

    return render(request,'app/filter.html')