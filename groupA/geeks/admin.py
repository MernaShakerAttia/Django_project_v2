from django.contrib import admin
from .models import category, forbidden,Post,Comment

# Register your models here.
admin.site.register(Post)
<<<<<<< HEAD
admin.site.register(category)

=======
admin.site.register(Comment)
admin.site.register(category)
# admin.site.register(user)
admin.site.register(forbidden)
>>>>>>> b22afb8259c5a0c8c249b1b579dce7962f899097
