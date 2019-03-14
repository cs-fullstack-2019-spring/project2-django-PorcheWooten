from django.contrib import admin
from .models import PostModel, RelatedItemsModel, WikiUserModel

# Register your models here.
admin.site.register(PostModel)
admin.site.register(RelatedItemsModel)
admin.site.register(WikiUserModel)