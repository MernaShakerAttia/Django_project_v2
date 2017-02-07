from django.contrib import admin
from .models import category, forbidden,Post,Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(category)
# admin.site.register(user)
admin.site.register(forbidden)


"""class PostCustom(admin.StackedInline):
    model = Post

    
    

class categoryCustom(admin.ModelAdmin):
    inlines = [PostCustom]

class categoryCustom2(admin.ModelAdmin):
	inlines = [PostCustom]
	list_display = ('contant','post_time', 'was_published_recently')
	search_fields = ['contant']
	list_filter = ['post_time']


admin.site.register(Post)
admin.site.register(category, categoryCustom2)"""
