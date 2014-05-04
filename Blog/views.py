import datetime

from django.shortcuts import render, get_object_or_404

from .models import Post, Tag, Comment
from .forms import CommentForm

def index(request):
    posts = Post.objects.all().order_by('created')[:10]
    tq = Tag.getTagsWithQuantity()
    return render(request, 'Blog/listOfPosts.html', {'posts':posts, 'tagsQuantity': tq})

def postByTag(request, tag):
    tag = Tag.objects.get(name=tag)
    posts = tag.post_set.all()
    tq = Tag.getTagsWithQuantity()
    return render(request, 'Blog/listOfPosts.html', {'posts':posts,'tagsQuantity': tq})

def postPage(request, postID):
    tq = Tag.getTagsWithQuantity()
    post = get_object_or_404(Post, pk=postID)
    comments = Comment.objects.all().filter(post=post)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm (request.POST)
        if form.is_valid():
            Comment(author = form.cleaned_data['author'],
                    body = form.cleaned_data['body'],
                    post=post,
                    created=datetime.datetime.now()).save()
    return render(request, 'Blog/postPage.html', {'post': post, 'comments':comments, 'form':form,
                                                  'tagsQuantity': tq})