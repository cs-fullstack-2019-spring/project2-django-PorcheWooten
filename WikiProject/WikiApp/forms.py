from django import forms
from .models import PostModel, RelatedItemsModel, WikiUserModel

class PostForm(forms.ModelForm):
    class Meta():
        model = PostModel
        exclude = ["foreignKeyToPost"]
        fields = '__all__'


class relatedItemsForm(forms.ModelForm):
    class Meta():
        model = RelatedItemsModel
        exclude = ["relatedItemForeignKey"]
        fields = '__all__'


class userForm(forms.ModelForm):
    class Meta():
        model = WikiUserModel
        exclude = ["userForeignKey"]
        fields = '__all__'

        def clean(self):
            pass1 = self.cleaned_data["password1"]
            pass2 = self.cleaned_data["password2"]

            if pass1 != pass2:
                raise forms.ValidationError('Password do no match, Try Again')
            return
