from django.contrib import admin

from .models import Category, Comment_Model, Model_Form, Post_in_Python

admin.site.register(Post_in_Python)
admin.site.register(Category)
admin.site.register(Model_Form)
admin.site.register(Comment_Model)