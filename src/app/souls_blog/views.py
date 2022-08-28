from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "souls_blog/home.html")

def blog(request):
    return render(request, "souls_blog/blog.html")

def post(request, id):
    return render(request, "souls_blog/post.html")