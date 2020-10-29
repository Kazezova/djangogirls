# Register your models here.
from django.contrib import admin
from .models import Post

admin.site.register(Post) #to make our model visible on the admin page