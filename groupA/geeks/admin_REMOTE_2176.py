from django.contrib import admin
from .models import category, forbidden, users,Post,Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(category)
admin.site.register(users)
admin.site.register(forbidden)
