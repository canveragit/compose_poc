from django.db import models

def user_directory_path(self, file_name):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'order_{0}/{1}'.format(self,file_name)

# Create your models here.
class Photobook(models.Model):
    co_id = models.AutoField(primary_key=True, unique=True)
    order_number = models.CharField(max_length=500)
    page_details = models.JSONField(max_length=500)
    version = models.CharField(max_length=500)
    created_at = models.DateField()
    updated_at = models.DateField() 

class ImageAlbum(models.Model):
    # co_id = models.ForeignKey(Photobook, related_name='order_no', on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    images = models.FileField(upload_to= user_directory_path)
    
    def __str__(self):
        return self.file_name
