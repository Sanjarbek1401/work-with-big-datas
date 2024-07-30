from django.contrib import admin
from .models import Category,Book,Author
from django.contrib.auth.models import User,Group

# Register your models here.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Author)
admin.site.unregister(Group)
admin.site.unregister(User)
