from django.contrib import admin
from .models import category, forbidden,Post,Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(category)
# admin.site.register(user)
admin.site.register(forbidden)
