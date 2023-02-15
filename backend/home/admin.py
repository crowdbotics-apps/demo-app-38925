from django.contrib import admin
from .models import Auth,Item,User
admin.site.register(Item)
admin.site.register(User)
admin.site.register(Auth)

# Register your models here.
