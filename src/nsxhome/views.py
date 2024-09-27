from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    my_context = {
        'day':'friday'
    }
    page_name="home.html"
    return render(request, page_name, my_context)