from django.contrib import admin

# Register your models here.
from .models import Post
admin.site.register(Post)
## help add menu page of http://127.0.0.1:8000/admin/