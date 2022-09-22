import os
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from Photobook.models import Photobook
from Photobook.serializers import PhotobookSerializers
from rest_framework.decorators import api_view


@api_view(['POST'])
def JSON_respone(request):
    if request.method == 'POST':
        photobook_data = JSONParser().parse(request)
        photobook_serializer = PhotobookSerializers(data=photobook_data)
        print(photobook_data,photobook_serializer,request)
    return JsonResponse(photobook_serializer.data, status=status.HTTP_201_CREATED) 
    
    

@api_view(['GET', 'POST', 'DELETE'])
def Photobook_list(request):
    #Retrieve all Photobooks/ find by order_number from PostgreSQL database:
    
    if request.method == 'GET':
        photobooks = Photobook.objects.all()
        
        order_number = request.GET.get('order_number', None)
        if order_number is not None:
            photobooks = photobooks.filter(order_number_contains=order_number)
        
        Photobook_Serializers = PhotobookSerializers(photobooks, many=True)
        return JsonResponse(Photobook_Serializers.data, safe=False)
        # 'safe=False' for objects serialization
        
    elif request.method == 'POST':
        photobook_data = JSONParser().parse(request)
        photobook_serializer = PhotobookSerializers(data=photobook_data)
        if photobook_serializer.is_valid():
            photobook_serializer.save()
            return JsonResponse(photobook_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(photobook_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Photobook.objects.all().delete()
        return JsonResponse({'message': '{} Photobook were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def Photobook_detail(request, order_number):
    # find photobook by order_number (order_number)
    
    try: 
        photobook = Photobook.objects.get(order_number=order_number) 
    except Photobook.DoesNotExist: 
        return JsonResponse({'message': 'The photobook does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        photobook_serializer = PhotobookSerializers(photobook) 
        return JsonResponse(photobook_serializer.data) 
    
    elif request.method == 'PUT': 
        photobook_data = JSONParser().parse(request) 
        photobook_serializer = PhotobookSerializers(photobook, data=photobook_data) 
        if photobook_serializer.is_valid(): 
            photobook_serializer.save() 
            order_folder(order_number)
            return JsonResponse(photobook_serializer.data) 
        return JsonResponse(photobook_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE': 
        photobook.delete() 
        return JsonResponse({'message': 'Photobook was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    
# Filter to find something specific like order status,version etc    
@api_view(['GET'])
def Photobook_list_published(request,version):
    # GET all photobooks
    
    photobooks = Photobook.objects.filter(version=version)
        
    if request.method == 'GET': 
        Photobook_Serializers = PhotobookSerializers(photobooks, many=True)
        return JsonResponse(Photobook_Serializers.data, safe=False)
    
def order_folder(order_id):
    current_path = os.getcwd()
    # print(current_path)
    list_folders = os.listdir()
    # print(list_folders)
    i = 0
    if i == 1: 
        if order_id in list_folders:
            pass
        else:
            os.mkdir(order_id)
        os.chdir(order_id)
        order_id_folders = os.listdir()
        if 'photobook_files' in order_id_folders:
            pass
        else:
            os.mkdir('photobook_files')
        os.chdir('photobook_files')
        
        # IMAGES PASTED IN THIS FOLDER 
        
        # os.chdir("\\")