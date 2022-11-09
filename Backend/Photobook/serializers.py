from rest_framework import serializers
from Photobook.models import Photobook
<<<<<<< Updated upstream
from Photobook.models import ImageAlbum


class PhotobookSerializers(serializers.ModelSerializer):
    class Meta: 
        model=Photobook
        fields = ('co_id', 'order_number', 'page_details', 'version', 'created_at', 'updated_at')

class ImageAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImageAlbum
        fields = ('file_name','images')

    
=======
>>>>>>> Stashed changes

# class PhotobookSerializers(serializers.Serializer):
    # co_id = serializers.IntegerField()
    # order_number = serializers.CharField()
    # page_details = serializers.JSONField()
    # version = serializers.CharField()
    # created_at = serializers.DateField
    # updated_at = serializers.DateField() 

    # def create(self, validated_data):
    #     Photobook_obj = Photobook(**validated_data)
    #     Photobook_obj.save()
    #     return Photobook_obj

    # def update(self, instance, validated_data):
    #     instance.name = validated_data["co_id"]
    #     instance.save()
    #     return instance
<<<<<<< Updated upstream
=======

class PhotobookSerializers(serializers.ModelSerializer):
    class Meta: 
        model=Photobook
        fields = ('co_id', 'order_number', 'page_details', 'version', 'created_at', 'updated_at')
>>>>>>> Stashed changes
    
# class ImageAlbumSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=ImageAlbum
<<<<<<< Updated upstream
#         field = ('order_number','images')
=======
#         field = ('co_id','image')
>>>>>>> Stashed changes
    