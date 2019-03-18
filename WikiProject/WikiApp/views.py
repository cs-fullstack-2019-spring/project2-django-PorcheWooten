from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm, PostModel, relatedItemsForm, RelatedItemsModel, userForm, WikiUserModel


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
        print("*", new_post, "*")
        img_file = ''
        if request.FILES:
            # print(request.POST)
            # print(request.FILES)
            # print('file attached')
            img_file = request.FILES['wiki_post_image']

        PostModel.objects.create(postSubject=request.POST['postSubject'], postText=request.POST['postText'],
                                 wiki_post_image=img_file, foreignKeyToPost=request.user)

        return redirect('YourPosts')
    context = {
        'new_post': new_post,

    }
    return render(request, 'WikiApp/NewPosts.html', context)


@login_required
def YourPosts(request):
    # allposts = PostModel.objects.all()
    context = {}

    if request.user.is_authenticated:
        # This puts the logged in user entry into the variable collector
        # wikiUser = WikiUserModel.objects.get(username=request.user)
        # This will grab all of the entries for the logged in user using the variable you just created

        wikiUser = request.user
        userPosts = PostModel.objects.filter(foreignKeyToPost=wikiUser)
        print(userPosts)
        # allRelatedPost = RelatedItemsModel.objects.all()
        # print(allRelatedPost)

        # context= {
        #     'allposts':userPosts
        # }
        # else:
        #     userPosts = ""
        #     allRelatedPost=""
        context = {
            'userPosts': userPosts
        }
    return render(request, 'WikiApp/YourPosts.html', context)


def editPost(request, post_id):
    posts = get_object_or_404(PostModel, pk=post_id)
    edit_post = PostForm(request.POST or None, instance=posts)
    if edit_post.is_valid():
        edit_post.save()
        return redirect('YourPosts')
    return render(request, 'WikiApp/NewPosts.html', {'new_post': edit_post})


def deletePost(request, post_id):
    posts = get_object_or_404(PostModel, pk=post_id)
    if request.method == "POST":
        posts.delete()
        return redirect('YourPosts')
    context = {
        "selectedPost": posts
    }
    return render(request, 'WikiApp/deletePost.html', context)


def newRelatedPost(request, post_id):
    relatedPost = relatedItemsForm(request.POST or None, request.FILES)
    if relatedPost.is_valid():
        relatedPost.save()
        relateditems = get_object_or_404(PostModel, pk=post_id)
        img_file = ''
        if request.FILES:
            # print(request.POST)
            # print(request.FILES)
            # print('file attached')
            img_file = request.FILES['relatedwiki_post_image']

        RelatedItemsModel.objects.create(relatedpostSubject=request.POST['relatedpostSubject'], relatedpostText=request.POST['relatedpostText'],
                                 relatedwiki_post_image=img_file, foreignKeyToPost=relatedPost)
        return redirect('viewpost')
    context = {

        'relatedPost': relatedPost,

    }

    return render(request, 'WikiApp/newRelatedPost.html', context)


def editRelatedItem(request, item_id):
    relatedPost = get_object_or_404(RelatedItemsModel, pk=item_id)
    edit_relatedItem = relatedItemsForm(request.POST or None, instance=relatedPost)
    if edit_relatedItem.is_valid():
        edit_relatedItem.save()
        return redirect('YourPosts')
    return render(request, 'WikiApp/newRelatedPost.html', {'relatedPost': edit_relatedItem})


def deleteRelatedItem(request, item_id):
    relatedPost = get_object_or_404(RelatedItemsModel, pk=item_id)
    if request.method == "POST":
        relatedPost.delete()
        return redirect('YourPosts')
    context = {
        "selectedItem": relatedPost
    }
    return render(request, 'WikiApp/deleteRelatedItem.html', context)


def NewUser(request):
    NewUser = userForm(request.POST or None)

    if request.method == 'POST':
        if NewUser.is_valid():
            user = WikiUserModel.objects.create(username=request.POST['username'], email=request.POST['email'], password1=request.POST['password1'])
            NewUser.save()
            return redirect('index')

    context = {
        'userform': NewUser,
    }
    return render(request, 'WikiApp/NewUser.html', context)


def viewpost(request, post_id):
    oldPost = get_object_or_404(PostModel, pk=post_id)
    relatedItems = RelatedItemsModel.objects.all()
    context = {
        'oldPost': oldPost,
        'relatedItems':relatedItems
    }
    return render(request, 'WikiApp/viewpost.html', context)
