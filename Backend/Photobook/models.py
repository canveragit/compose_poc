from django.db import models

def user_directory_path(self, file_name):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'order_{0}/photobookfiles/{1}'.format(self,file_name)

# Create your models here.
class Photobook(models.Model):
    co_id = models.AutoField(primary_key=True, unique=True)
    order_number = models.CharField(max_length=500)
    page_details = models.JSONField(max_length=500)
    version = models.CharField(max_length=500)
    created_at = models.DateField()
<<<<<<< Updated upstream
    updated_at = models.DateField() 

class ImageAlbum(models.Model):
    # co_id = models.ForeignKey(Photobook, related_name='order_no', on_delete=models.CASCADE)
    file_name = models. CharField(max_length=255)
    images = models.FileField(upload_to= user_directory_path)
    
    def __str__(self):
        return self.file_name

# class ImageAlbum(models.Model):
#     album = models.ForeignKey(Photobook, related_name='order_sl', on_delete=models.CASCADE)
#     images = models.ImageField(upload_to= user_directory_path)
=======
    updated_at = models.DateField(timezone.now) 
    # ImageAlbum = None
    
    # image = models.ImageField(upload_to='images/')
    # image = models.FileField(upload_to = user_directory_path)
    
    # # Creates a folder 
    # def save(self, *args, **kwargs):
    #     os.mkdir("ORDER-{}".format(self.order_number))
    #     return super().save(*args, **kwargs)

    
# class ImageAlbum(models.Model):
#     album = models.ForeignKey(Photobook, related_name='order_sl', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to= user_directory_path)
>>>>>>> Stashed changes
#     # image = models.ImageField(upload_to='images/')
    
#     def save(self, *args, **kwargs):
#        return super(ImageAlbum, self).save(*args, **kwargs)
    
#     def default(self):
#         return self.images.filter(default=True).first()
<<<<<<< Updated upstream
 
=======
    
>>>>>>> Stashed changes
