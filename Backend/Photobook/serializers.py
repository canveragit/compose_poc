from rest_framework import serializers
from Photobook.models import Photobook

from rest_framework import serializers
from Photobook.models import Photobook

class PhotobookSerializers(serializers.ModelSerializer):
    class Meta: 
        model=Photobook
        fields = ('co_id', 'order_number', 'page_details', 'version', 'created_at', 'updated_at')

    

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
    
# class ImageAlbumSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=ImageAlbum
#         field = ('order_number','images')
    