from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm, ImageForm, ImageFormSet
from django.contrib.auth.decorators import login_required
from django.db import transaction

# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES)
        if form.is_valid() and image_formset.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            with transaction.atomic():
                post.save()
                image_formset.instance = post
                image_formset.save()
                print(image_formset)
                return redirect('posts:index')
    else:
        form = PostForm()
        image_form = ImageFormSet()
    context = {
        'form': form,
        'image_form': image_form
    }
    return render(request, 'posts/form.html', context)

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('posts:detail', id)
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form
    }
    return render(request, 'posts/detail.html', context)

def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('posts:detail', post_id)