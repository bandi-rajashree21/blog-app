from django.shortcuts import render,get_object_or_404
from .models import Post
from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})


from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form})


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post")

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'blog/delete_post.html', {'post': post})
