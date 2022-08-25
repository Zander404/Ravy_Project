from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "souls_blog/home.html")