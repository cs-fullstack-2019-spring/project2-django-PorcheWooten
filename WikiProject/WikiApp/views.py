from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, PostModel,relatedItemsForm,RelatedItemsModel, WikiUserModel, userForm
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    allposts = PostModel.objects.all()
    allRelatedPost = RelatedItemsModel.objects.all()
    context = {
        'allposts': allposts,
        'allRelatedPost': allRelatedPost
    }
    return render(request, 'WikiApp/index.html', context)

@login_required
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

@login_required
def YourPosts(request):
    allposts = PostModel.objects.all()
    allRelatedPost = RelatedItemsModel.objects.all()
    context = {
        'allposts': allposts,
        "allRelatedPost": allRelatedPost
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


def newRelatedPost(request):
    relatedPost = relatedItemsForm(request.POST or None)
    if relatedPost.is_valid():
        relatedPost.save()
        return redirect ('YourPosts')

    context = {

        'relatedPost':relatedPost
    }

    return render(request, 'WikiApp/newRelatedPost.html', context)



def editRelatedItem(request,id):
    relatedPost = get_object_or_404(RelatedItemsModel, pk=id)
    edit_relatedItem = relatedItemsForm(request.POST or None, instance=relatedPost)
    if edit_relatedItem.is_valid():
        edit_relatedItem.save()
        return redirect('YourPosts')
    return render (request, 'WikiApp/newRelatedPost.html', {'relatedPost': edit_relatedItem})

def deleteRelatedItem(request,id):
    relatedPost = get_object_or_404(RelatedItemsModel, pk=id)
    if request.method == "POST":
        relatedPost.delete()
        return redirect('YourPosts')
    context={
        "selectedItem": relatedPost
    }
    return render (request, 'WikiApp/deleteRelatedItem.html', context)

def NewUser(request):
    NewUser = userForm(request.POST or None)
    if NewUser.is_valid():
        # NewUser.save()
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
        # user.save()
        return redirect('index')
    context = {
        'userform': NewUser,
    }
    return render(request, 'WikiApp/NewUser.html', context)