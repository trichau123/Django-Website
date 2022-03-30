from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

posts = [
    {
    'author' : 'Trichau',
    'title': 'blog post 1',
    'content' : 'First post content',
    'date_posted': 'August 27, 2021'
    },
    {
    'author' : 'Mikey',
    'title': 'blog post 1',
    'content' : 'second post content',
    'date_posted': 'Janurary 30, 2021'
    },
    {
    'author' : 'Tony',
    'title': 'blog post 1',
    'content' : 'First post content',
    'date_posted': 'August 02, 2020'
    }
]
def home(request):
    #dictionary context
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})