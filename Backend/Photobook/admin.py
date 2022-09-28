from django.contrib import admin
from .models import ImageAlbum, Photobook
# Register your models here.

admin.site.register(Photobook)
admin.site.register(ImageAlbum)