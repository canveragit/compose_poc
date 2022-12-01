from django.contrib import admin
from .models import Photobook
from Photobook.models import ImageAlbum

# Register your models here.
admin.site.register(Photobook)
admin.site.register(ImageAlbum)
