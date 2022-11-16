from rest_framework import serializers
from Photobook.models import Photobook
from Photobook.models import ImageAlbum

class PhotobookSerializers(serializers.ModelSerializer):
    class Meta: 
        model=Photobook
        fields = ('co_id', 'order_number', 'page_details', 'version', 'created_at', 'updated_at')

class ImageAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImageAlbum
        fields = ('file_name','images')

    