from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.User)
admin.site.register(models.giftcard)
# admin.site.register(models.Post)