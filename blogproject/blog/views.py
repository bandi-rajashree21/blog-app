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
