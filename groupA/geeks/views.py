from django.shortcuts import render
from .models import category, Post
from django.http import HttpResponse ,HttpResponseRedirect

# Create your views here.

def show_all_categorys(request):
	all_cat = category.objects.all()
	context = {'all_categorys': all_cat}
	return render(request, 'geeks/index.html' ,context)

def show_posts(request,id):
	all_post = Post.objects.filter(post_category=id)
	context = {'all_posts': all_post}
	return render(request, 'geeks/show_all_posts.html' ,context)

def details(request,id):
    post = Post.objects.get(id=id)
    context = {'spacific_post':post}
    return render(request, 'geeks/show_post.html' ,context)
