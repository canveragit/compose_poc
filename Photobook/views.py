
## Method 1

# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse

# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view

# from Photobook.models import Photobook
# from Photobook.serializers import PhotobookSerializers

# @api_view(['POST'])
# def add_PhotobookAPI(request):
#     Photobook_data=JSONParser().parse(request)  
#     Photobook_Serializer=PhotobookSerializers(data=Photobook_data)
#     if Photobook_Serializer.is_valid():
#         print(Photobook_Serializer)
#         Photobook_Serializer.save
#         return Response({"status": "success", "data": Photobook_Serializer.data}, status=status.HTTP_200_OK)
#     # return JsonResponse("Failed to Insert", safe=False, status=400)
#     else:
#         error_details = []
#         for key in Photobook_Serializer.errors.keys():
#             error_details.append({"field": key, "message": Photobook_Serializer.errors[key][0]})

#         data = {
#                 "Error": {
#                     "status": 400,
#                     "message": "Your submitted data was not valid - please correct the below errors",
#                     "error_details": error_details
#                     }
#                 }

#         return Response(data, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'POST'])
# def update_photobook(request, co_id):
#     # photobook_obj = Photobook.objects.get(co_id=co_id)

#     if request.method == "GET":
        
#         Photo_books = Photobook.objects.all()
#         Photobook_Serializer = PhotobookSerializers(Photo_books,many=True)
#         return JsonResponse(Photobook_Serializer.data,safe=False)
    
#         # photobook_data = PhotobookSerializers(photobook_obj, many=True).data
#         # return Response({"data": photobook_data}, status=status.HTTP_200_OK)
#     elif request.method == "DELETE":
#         photobook_obj = Photobook.objects.get(co_id=co_id)
#         photobook_obj.delete()
#         return Response({"data": "Photobook Deleted Successfully."}, status=status.HTTP_200_OK)
#     else:
#         photobook_obj = Photobook.objects.get(co_id=co_id)
#         photobook_serializer = PhotobookSerializers(photobook_obj, data=request.data)
#         if photobook_serializer.is_valid():
#             photobook_serializer.save()
#             return Response({"data": "Photobook Updated successfully"}, status=status.HTTP_200_OK)
#         else:
#             error_details = []
#             for key in photobook_serializer.errors.keys():
#                 error_details.append({"field": key, "message": photobook_serializer.errors[key][0]})
#             data = {
#                     "Error": {
#                         "status": 400,
#                         "message": "Your submitted data was not valid - please correct the below errors",
#                         "error_details": error_details
#                         }
#                     }

#             return Response(data, status=status.HTTP_400_BAD_REQUEST)

## Method 2

# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse

# from rest_framework.response import Response
# from rest_framework import status

# from Photobook.models import Photobook
# from Photobook.serializers import PhotobookSerializers

# @csrf_exempt
# def PhotobookAPI(request,co_id=0):
#     if request.method == 'GET':
#         Photo_books = Photobook.objects.all()
#         Photobook_Serializer = PhotobookSerializers(Photo_books,many=True)
#         return JsonResponse(Photobook_Serializer.data,safe=False)
#     elif request.method=='POST':
#         Photobook_data=JSONParser().parse(request)  
#         Photobook_Serializer=PhotobookSerializers(data=Photobook_data)
#         if Photobook_Serializer.is_valid():
#             Photobook_Serializer.save
#             return Response({"status": "success", "data": Photobook_Serializer.data}, status=status.HTTP_200_OK)
#         return JsonResponse("Failed to Insert", safe=False, status=400)
#     elif request.method=='PUT':
#         Photobook_data=JSONParser().parse(request)
#         Photobooks = Photobook.objects.get(co_id=co_id)
#         Photobook_Serializer=PhotobookSerializers(Photobooks,data=Photobook_data)
#         if Photobook_Serializer.is_valid():
#             Photobook_Serializer.save()
#             return JsonResponse("Update Successfully",safe=True)
#         return JsonResponse("Failed to Update")
#     elif request.method=='DELETE':
#         Photobooks=Photobook.objects.get(co_id=co_id)
#         Photobooks.delete()
#         return JsonResponse("Delete Successfully",safe=False)

# Method 3 

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from Photobook.models import Photobook
from Photobook.serializers import PhotobookSerializers
from rest_framework.decorators import api_view


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
def Photobook_detail(request, co_id):
    # find photobook by co_id (co_id)
    
    try: 
        photobook = Photobook.objects.get(co_id=co_id) 
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