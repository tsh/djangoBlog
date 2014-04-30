from django.shortcuts import render

from .models import Post

def index(request):
    posts = Post.objects.all().order_by("created")[:10]
    return render(request, 'Blog/index.html', {'posts':posts})
