from django.shortcuts import render

# Create your views here.
def display(req):
    return render(req,'index.html')
