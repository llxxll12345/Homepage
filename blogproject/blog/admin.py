from django.contrib import admin
from .models import Post, Category, Tag
# register models here

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'category', 'author', 'modified_time']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)