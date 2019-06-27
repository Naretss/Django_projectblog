from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'Narets',
        'title':'Blog Post 1',
        'content': 'First post content',
        'date_posted':'August 27,2018'
    },
        {
        'author':'Namwhan',
        'title':'Blog Post 2',
        'content': 'Second post content',
        'date_posted':'August 28,2018'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blogg/home.html',context)


def about(request):
    return render(request,'blogg/about.html',{'title':'About'})
