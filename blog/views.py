# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') #QuerySet
    for i in range(len(posts)):
        if i==0:
            posts[i].active = 'active'
        else:
            posts[i].active = ''
    return render(request, 'blog/index.html', {'posts': posts[:5]})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES,)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') #QuerySet
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_search(request):
    if request.method == "POST":
        posts = Post.objects.filter(text__contains=request.POST['search'])
        return render(request, 'blog/post_list.html', {'posts': posts})