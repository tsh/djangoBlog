from django.shortcuts import render, get_object_or_404

from .models import Post, Tag

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
    post = get_object_or_404(Post, pk=postID)
    return render(request, 'Blog/postPage.html', {'post': post})