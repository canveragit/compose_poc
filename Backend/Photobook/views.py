from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from Photobook.models import ImageAlbum
from Photobook.serializers import ImageAlbumSerializer
from Photobook.models import Photobook
from Photobook.serializers import PhotobookSerializers
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from Photobook import models

from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from rest_framework.response import Response

@csrf_exempt
def index(request):
    return render(request,"index.html")

@csrf_exempt
def OrderUpload(self,request,*args,**kwargs):
    if request.method == "POST" :
        file_s=ImageAlbumSerializer(data=request.data)
        print("-----------")
        print(request)
        print("-----------")
        # print(order_no)
        print(file_s)
        print(type(file_s))
        print("-----------")

        if file_s.is_valid():
            file_s.save()
            return Response(file_s.data,status=status.HTTP_201_CREATED)

        else:
            print('error',file_s.errors)
            return Response(file_s.errors,status=status.HTTP_400_BAD_REQUEST)
        
        # filename = str(myfile)
        # with default_storage.open(filename + '/photobookfiles/', 'wb+') as destination:
        # # with FileSystemStorage.open(base_url = "filename + '/photobookfiles/' ", file_permissions_mode ='wb+') as destination:
        #     for file in myfile.chunks():
        #         destination.write(file)
        # return response("ok", status=status.HTTP_200_OK)


# @csrf_exempt
# def OrderUpload(request):
#     if request.method == "POST" :
#         order_no = request.POST.get("order_number")
#         myfile = request.FILES.getlist("uploadfiles")
#         for f in myfile:
#             # models.ImageAlbum(file_name = order_no,images=f).save()
#             a = models.ImageAlbum(file_name = order_no,images=f)
#         return HttpResponse("Successfully Uploaded ")

@csrf_exempt    
def ImageView(request,file_name):

    if request.method == "GET" : 
        images = ImageAlbum.objects.all()
    
        file_name = request.GET.get('file_name', None)
        if file_name is not None:
            images = images.filter(file_name_contains=file_name)

        ImageAlbum_Serializer = ImageAlbumSerializer(images, many=True)
        return JsonResponse(ImageAlbum_Serializer.data, safe=False, 
        status=status.HTTP_201_CREATED)

    # try: 
    #     images = ImageAlbum.objects.get(file_name=file_name) 
    # except Photobook.DoesNotExist: 
    #     return JsonResponse({'message': 'The image file name does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    # if request.method == 'GET': 
    #     ImageAlbum_Serializer = ImageAlbumSerializer(images) 
    #     return JsonResponse(ImageAlbum_Serializer.data, safe=False) 

# (GET)    photobook                        - to get all the photobooks
# (GET)    photobook/<co_id>                - to get a specific order
# (POST)   photobook                        - to add new order 
# (PUT)    photobook/<co_id>                - To update an existing Photobook
# (DELETE) photobook/<co_id>                - To remove a photobook with <co_id>
# (DELETE) photobook                        - To remove all the orders
# (GET)    photobook/<version>              - To filter all the orders version vise 
# (GET)    photobook?order_number=[IC-1234] - To filter order_number from Photobook

@api_view(['GET', 'POST', 'DELETE'])
def Photobook_list(request):
    
    # Retrieve all Photobooks
    if request.method == 'GET':
        photobooks = Photobook.objects.all()
        
        order_number = request.GET.get('order_number', None)
        if order_number is not None:
            photobooks = photobooks.filter(order_number_contains=order_number)
        
        Photobook_Serializers = PhotobookSerializers(photobooks, many=True)
        return JsonResponse(Photobook_Serializers.data, safe=False, 
        status=status.HTTP_201_CREATED)
        # 'safe=False' for objects serialization
    
    # Inserting a new record   
    elif request.method == 'POST':
        photobook_data = JSONParser().parse(request)
        photobook_serializer = PhotobookSerializers(data=photobook_data)
        if photobook_serializer.is_valid():
            photobook_serializer.save()
            
            return JsonResponse(photobook_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(photobook_serializer.errors, status=status.HTTP_400_BAD_REQUEST,safe=False)
    
    # Delete all records
    elif request.method == 'DELETE':
        count = Photobook.objects.all().delete()
        return JsonResponse({'message': '{} Photobook were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def Photobook_detail(request, co_id):
    try: 
        photobook = Photobook.objects.get(co_id=co_id) 
    except Photobook.DoesNotExist: 
        return JsonResponse({'message': 'The photobook does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    # Find photobook by co_id
    if request.method == 'GET': 
        photobook_serializer = PhotobookSerializers(photobook) 
        return JsonResponse(photobook_serializer.data, safe=False) 
    
    # Changing a single record respective to the co_id given in the request
    elif request.method == 'PUT': 
        photobook_data = JSONParser().parse(request) 
        photobook_serializer = PhotobookSerializers(photobook, data=photobook_data) 
        if photobook_serializer.is_valid(): 
            photobook_serializer.save() 
            return JsonResponse(photobook_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(photobook_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    # Deleting a singe record respective to the co_id given to the request
    elif request.method == 'DELETE': 
        photobook.delete() 
        return JsonResponse({'message': 'Photobook was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    
# Filter to find something specific like order status,version etc    
@api_view(['GET'])
def Photobook_version(request,version):
    
    photobooks = Photobook.objects.filter(version=version)
    # GET all photobooks 
    if request.method == 'GET': 
        Photobook_Serializers = PhotobookSerializers(photobooks, many=True)
        return JsonResponse(Photobook_Serializers.data, safe=False)
        