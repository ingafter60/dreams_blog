from django.shortcuts import render
from .models import Post
from marketing.models import Signup

def index(request):
    # queryset = Post.objects.filter(featured=True)
    featured = Post.objects.filter(featured=True)
    latest   = Post.objects.order_by('-timestamp')[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context  = {
        # 'object_list' : queryset
        'object_list' : featured,
        'latest' : latest
    }
    return render(request, 'index.html', context)

def blog(request):
    return render(request, 'blog.html', {})

def post(request):
    return render(request, 'post.html', {})

