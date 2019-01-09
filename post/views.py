from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostModelForm

# Create your views here.

def index(request):
    context = {}
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request, 'index.html', context)

def detail(request, post_id):
    context={}
    context['post'] = Post.objects.get(id=post_id)
    return render(request, 'detail.html', context)

def update(request, post_id):
    context = {}
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponse('Post updated.')
        else:
            context['form'] = form
            render(request, 'update.html', context)
    else:
        context['form'] = PostModelForm(instance=post)
    return render(request, 'update.html', context)
