from django.shortcuts import render
from polls.models import Posts
# Create your views here.


def index(request) :

    tmp = Posts.objects.all()
    context = {"posts_list" : tmp}

    return render(request,'index.html',context)

def content(request) :
    pass

def write(request) :
    tmp = 3
    context = {"test" : tmp}
    return render(request,'write.html',context)
