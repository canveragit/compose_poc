import os
from django.db import models
from datetime import datetime

def user_directory_path(instance, filename):
    time = datetime.now()
    basefilename, file_extension= os.path.splitext(filename)
    ord = instance.folder_name
    path = str(os.path("/media/{ord}/".format(ord=ord)))
    if ord in path:
        print ("yes")
    else:
        print("No")

    basefilename = "File-"
    
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return '{0}/{1}{2}'.format(instance.folder_name, basefilename, file_extension)

# Create your models here.
class Photobook(models.Model):
    co_id = models.AutoField(primary_key=True,unique=True)
    order_number = models.CharField(unique=True, max_length=500)

class ImageAlbum(models.Model):
    folder_name = models.CharField(max_length=255)
    images = models.FileField(upload_to= user_directory_path)






# from django.db import models
# from datetime import datetime

# def user_directory_path(self, file_name):
#     time = datetime.now()
#     # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
#     return '{0}/{1}/{2}/{3}/photobookfiles/{4}'.format(time.strftime("%Y"), time.strftime("%m"), time.strftime("%d"),self,file_name)

# # Create your models here.
# class Photobook(models.Model):
#     co_id = models.AutoField(primary_key=True, unique=True)
#     order_number = models.CharField(max_length=500)
#     page_details = models.JSONField(max_length=500)
#     version = models.CharField(max_length=500)
#     created_at = models.DateField()
#     updated_at = models.DateField() 

# class ImageAlbum(models.Model):
#     # co_id = models.ForeignKey(Photobook, null=True, on_delete=models.CASCADE)
#     file_name = models.CharField(max_length=255)
#     images = models.FileField(upload_to= user_directory_path)
    
    # def __str__(self):
    #     return self.file_name

# class ImageAlbum(models.Model):
#     album = models.ForeignKey(Photobook, related_name='order_sl', on_delete=models.CASCADE)
#     images = models.ImageField(upload_to= user_directory_path)
#     # image = models.ImageField(upload_to='images/')
    
#     def save(self, *args, **kwargs):
#        return super(ImageAlbum, self).save(*args, **kwargs)
    
#     def default(self):
#         return self.images.filter(default=True).first()
