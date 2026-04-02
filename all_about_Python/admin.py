from django.contrib import admin

from .models import Category, Comment_Model, Idea, Post_in_Python

admin.site.register(Post_in_Python)
admin.site.register(Category)
admin.site.register(Idea)
admin.site.register(Comment_Model)