from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "souls_blog/home.html")

def blog(request):
    return render(request, "souls_blog/blog.html")


def erro404(request):
    return render(request, "souls_blog/erro404.html")