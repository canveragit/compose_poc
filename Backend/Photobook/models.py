import json
import os
from pyexpat import model
from venv import create
from django.db import models
from django.utils import timezone


# def save(self, *args, **kwargs):
#     os.mkdir("{}".format(self.order_number))
#     os.chdir(self.order_number)
#     os.mkdir('photobook_files')
#     return save(*args, **kwargs)


def __str__(self):
    return self.album


def user_directory_path(self, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'order_{0}/{1}'.format(self.album, filename)

    
class Photobook(models.Model):
    co_id = models.AutoField(primary_key=True, unique=True)
    order_number = models.CharField(max_length=500)
    page_details = models.JSONField(max_length=500)
    version = models.CharField(max_length=500)
    created_at = models.DateField()
    updated_at = models.DateField(timezone.now) 
    ImageAlbum = None
    
    # image = models.ImageField(upload_to='images/')
    # image = models.FileField(upload_to = user_directory_path)
    
    # # Creates a folder 
    # def save(self, *args, **kwargs):
    #     os.mkdir("ORDER-{}".format(self.order_number))
    #     return super().save(*args, **kwargs)

    
class ImageAlbum(models.Model):
    album = models.ForeignKey(Photobook, related_name='order_sl', on_delete=models.CASCADE)
    image = models.ImageField(upload_to= user_directory_path)
    # image = models.ImageField(upload_to='images/')
    
    def save(self, *args, **kwargs):
       return super(ImageAlbum, self).save(*args, **kwargs)
    
    def default(self):
        return self.images.filter(default=True).first()
    