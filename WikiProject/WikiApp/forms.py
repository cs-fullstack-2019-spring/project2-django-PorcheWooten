from django import forms
from .models import PostModel, RelatedItemsModel

class PostForm(forms.ModelForm):
    class Meta():
        model = PostModel
        fields = '__all__'

class relatedItemsForm(forms.ModelForm):
    class Meta():
        model = RelatedItemsModel
        fields = '__all__'