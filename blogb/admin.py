from django.contrib import admin
# Register your models here.

from .models import BlogSet, Content, Category, Author, TechNow

admin.site.register(TechNow)
admin.site.register(Author)
admin.site.register(BlogSet)
admin.site.register(Category)
admin.site.register(Content)

