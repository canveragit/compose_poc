from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from Photobook.models import Photobook
from Photobook.serializers import PhotobookSerializers

@api_view(['POST'])
def add_PhotobookAPI(request):
    Photobook_data=JSONParser().parse(request)  
    Photobook_Serializer=PhotobookSerializers(data=Photobook_data)
    if Photobook_Serializer.is_valid():
        print(Photobook_Serializer)
        Photobook_Serializer.save
        return Response({"status": "success", "data": Photobook_Serializer.data}, status=status.HTTP_200_OK)
    # return JsonResponse("Failed to Insert", safe=False, status=400)
    else:
        error_details = []
        for key in Photobook_Serializer.errors.keys():
            error_details.append({"field": key, "message": Photobook_Serializer.errors[key][0]})

        data = {
                "Error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                    }
                }

        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def update_photobook(request, co_id):
    # photobook_obj = Photobook.objects.get(co_id=co_id)

    if request.method == "GET":
        
        Photo_books = Photobook.objects.all()
        Photobook_Serializer = PhotobookSerializers(Photo_books,many=True)
        return JsonResponse(Photobook_Serializer.data,safe=False)
    
        # photobook_data = PhotobookSerializers(photobook_obj, many=True).data
        # return Response({"data": photobook_data}, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        photobook_obj = Photobook.objects.get(co_id=co_id)
        photobook_obj.delete()
        return Response({"data": "Photobook Deleted Successfully."}, status=status.HTTP_200_OK)
    else:
        photobook_obj = Photobook.objects.get(co_id=co_id)
        photobook_serializer = PhotobookSerializers(photobook_obj, data=request.data)
        if photobook_serializer.is_valid():
            photobook_serializer.save()
            return Response({"data": "Photobook Updated successfully"}, status=status.HTTP_200_OK)
        else:
            error_details = []
            for key in photobook_serializer.errors.keys():
                error_details.append({"field": key, "message": photobook_serializer.errors[key][0]})
            data = {
                    "Error": {
                        "status": 400,
                        "message": "Your submitted data was not valid - please correct the below errors",
                        "error_details": error_details
                        }
                    }

            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
