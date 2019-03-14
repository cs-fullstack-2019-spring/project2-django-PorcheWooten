from django.shortcuts import render,get_object_or_404,redirect

from .forms import PostForm, PostModel,relatedItemsForm,RelatedItemsModel


# Create your views here.

def index(request):
    allposts = PostModel.objects.all()
    context = {
        'allposts': allposts
    }
    return render(request, 'WikiApp/index.html', context)


def NewPosts(request):
    new_post = PostForm(request.POST or None)
    if new_post.is_valid():
        new_post.save()
        print("saved")
        return redirect('YourPosts')
    context={
        'new_post': new_post,

    }
    return render(request, 'WikiApp/NewPosts.html', context)


def YourPosts(request):
    allposts = PostModel.objects.all()
    context = {
        'allposts': allposts
    }
    return render(request, 'WikiApp/YourPosts.html', context)

def editPost(request,id):
    posts = get_object_or_404(PostModel, pk=id)
    edit_post = PostForm(request.POST or None, instance=posts)
    if edit_post.is_valid():
        edit_post.save()
        return redirect('YourPosts')
    return render (request, 'WikiApp/NewPosts.html', {'new_post': edit_post})



def deletePost(request,id):
    posts = get_object_or_404(PostModel, pk=id)
    if request.method == "POST":
        posts.delete()
        return redirect('YourPosts')
    context={
        "selectedPost": posts
    }
    return render (request, 'WikiApp/deletePost.html', context)

