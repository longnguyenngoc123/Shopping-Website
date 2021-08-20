from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import FoodForm 
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

class PostListView(ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = 'blog/blog.html'
    context_object_name = 'Post'
    paginate_by = 5

def productdetail(request, id):
    product = Post.objects.get(id=id)
    return render(request, 'blog/pdetail.html', {'data':product})

@user_passes_test(lambda u: u.is_superuser)
def emp(request):  
    if request.method == "POST":  
        form = FoodForm(request.POST,request.FILES) 
        print("Food Form: ",request.POST) 
        if form.is_valid():
              
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = FoodForm()  
    return render(request,'blog/add.html',{'form':form})  
@user_passes_test(lambda u: u.is_superuser)
def destroy(request, id):  
    post = Post.objects.get(id=id)  
    post.delete()  
    return redirect("/")  
@user_passes_test(lambda u: u.is_superuser)
def edit(request, id):  
    post = Post.objects.get(id=id)  
    return render(request,'blog/edit.html', {'post':post}) 
@user_passes_test(lambda u: u.is_superuser)
def update(request, id):  
    post = Post.objects.get(id=id)  
    form = FoodForm(request.POST,request.FILES,instance = post)  
    if form.is_valid():
        print("Food Form: ",request.POST)
        form.save()  
        return redirect("/")  
    return render(request, 'blog/edit.html', {'post': post})  