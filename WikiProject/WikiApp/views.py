from django.shortcuts import render

from .forms import PostForm, PostModel,relatedItemsForm,RelatedItemsModel


# Create your views here.

def index(request):
    return render(request, 'WikiApp/index.html')


def NewPosts(request):
    new_post = PostForm(request.POST or None)
    newRelatedItem = relatedItemsForm(request.POST or None)
    if new_post.is_valid() or newRelatedItem.is_valid():
        new_post.save() or newRelatedItem.save()
    context={
        'new_post': new_post,
        'newRelatedItem': newRelatedItem
    }
    return render(request, 'WikiApp/NewPosts.html', context)


def YourPosts(request):
    allposts = PostModel.objects.all()
    context = {
        'allposts': allposts
    }
    return render(request, 'WikiApp/YourPosts.html', context)
