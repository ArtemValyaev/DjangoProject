from django.contrib import admin
from .models import Articles, LikesDislikes, Categories, Comment

admin.site.register(Articles)
admin.site.register(LikesDislikes)
admin.site.register(Categories)
admin.site.register(Comment)
