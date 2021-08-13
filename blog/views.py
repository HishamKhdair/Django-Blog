from django.shortcuts import render
from .models import Post
from .forms import CreatePostForm

def home(request):
    context={
        'posts':Post.objects.all()
        }
    # you have to pass the argument as a dictionary here! you will pass what is in { }
    return render(request, 'blog/home.html' , context)


def about(request):
    return render(request, 'blog/about.html', {'title':'ABOUT'})

def create(request):
    if request.method == 'POST':
        form=CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            
    form=CreatePostForm()
    return render(request, 'blog/create.html', {'form':form})
