from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . models import Cast
from rest_framework.decorators import api_view
from . serializer import CastSerializer
from rest_framework.response import Response
# Create your views here.
from rest_framework import status


# Api method (http methods)
# 1)Get
# 2)Post
# 3)Put
# 4)Patch
# 5)delete


@api_view(['GET'])
def getalldata(request):
    data=Cast.objects.all()
    print(type(data))
    ser=CastSerializer(data,many=True)
    print(type(ser))
    ser_data=ser.data
    print(type(ser_data))
    return Response(ser_data)

@api_view(['GET'])
def filterldata(request):
    data=Cast.objects.all()  #virat,rohit,msdtt
    ser=CastSerializer(data,many=True)
    ser_data=ser.data    #virat,rohit,msdtt json listserilizer
    li=[]
    for i in ser_data:
        li.append(i['name'])

    return Response(li)
    # return Response(data)
#
#     for i in ser_data:
#         data=i['name']  # virat ,rohit
#         if data=="virat":
#             return Response(i)
#         else:
#             return Response(errror)

# 1)virat,rohit
# 2)name=="virat" show all data for virat(id,name,city,age)/ try with orm queery


@api_view(['POST'])
def creat_save(request):
    ser = CastSerializer(data=request.data)   # name city age
    if ser.is_valid():
        ser.save()
        return Response(ser.data,status=status.HTTP_201_CREATED)
    return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request,pk):   #id ,name,city  HW
    try:
        data=Cast.objects.get(pk=pk)
    except Cast.DoesNotExits:
        return Response({"error":"id not found"},status=status.HTTP_404_NOT_FOUND)

    ser = CastSerializer(data,data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    return Response (ser.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def filterldata2(request):
    name_to_filter = request.GET.get('name', None)  #age,city,id        (user reqest = "rohit")  HW

    if name_to_filter:
        # Filter data based on the 'name' field
        filtered_data = Cast.objects.filter(name=name_to_filter)
        ser = CastSerializer(filtered_data, many=True)
        return Response(ser.data)
    else:
        return Response({"error": "Please provide a 'name' parameter in the query string."})



@api_view(['GET'])
def filterldata3(request):
    data=Cast.objects.all()  #virat,rohit,msdtt
    ser=CastSerializer(data,many=True)
    ser_data=ser.data    #virat,rohit,msdtt json listserilizer
    li=[]
    for i in ser_data:
        if i['name']=="virat":
            li.append(i['name'])
            return Response(i)
        else:
            return Response ({"Info":"Not found"})


@api_view(['GET'])
def filterldata2(request):
    name_to_filter = request.GET.get('name', None)  #age,city,id        (user reqest = "rohit")

    if name_to_filter:
        # Filter data based on the 'name' field
        filtered_data = Cast.objects.filter(name=name_to_filter)
        ser = CastSerializer(filtered_data, many=True)
        return Response(ser.data)
    else:
        return Response({"error": "Please provide a 'name' parameter in the query string."})

# @api_view(['DELETE'])
# def deletedata(request):
#     id_to_delete= request.data.get('id',None)
#     if id_to_delete is None:
#         return Response({"error": "Please provide a 'id' parameter in the query string. for delete,id not found "})
#     try:
#         delete_data=Cast.objects.get(id=id_to_delete)
#         delete_data.delete()
#         return Response ({"msg":"succesfully delete"})
#     except:
#         return Response({"error": "Please provide a 'id' parameter in the query string. for delete,id not found "})

# from django.views.decorators.http import require_http_methods

# @api_view(['DELETE'])
# def deletedata(request):
#     id_to_delete = request.data.get('id', None)
#     if id_to_delete is None:
#         return Response({"error": "Please provide a 'id' parameter in the query string."}, status=400)  # Explicit 400 status code
#     try:
#         delete_data = Cast.objects.get(id=id_to_delete)
#         delete_data.delete()
#         return Response({"msg": "Successfully deleted"}, status=200)  # Explicit 200 status code
#     except Cast.DoesNotExist:
#         return Response({"error": "Cast object with the specified ID does not exist."}, status=404)
#     except Exception as e:
#         return Response({"error": "An unexpected error occurred: {}".format(e)}, status=500)  # Handle other errors


@api_view(['DELETE'])
def deletedata(request,pk):   #id ,name,city
    try:
        data=Cast.objects.get(pk=pk)
        data.delete()
        return Response({"msg": "Cast data deleted successfully"})
    except :
        return Response({"error":"id not found"},status=status.HTTP_404_NOT_FOUND)

    # return Response (ser.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def deletedata(request, pk):
#     try:
#         data = Cast.objects.get(pk=pk)
#         data.delete()  # Delete the object directly
#         return Response({"msg": "Cast data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#
#     except Cast.DoesNotExist:
#         return Response({"error": "Cast data with the specified ID does not exist"}, status=status.HTTP_404_NOT_FOUND)





@api_view(['PATCH'])
def update_partialy(request,pk):
    try:
        data=Cast.objects.get(pk=pk)
        ser = CastSerializer(data,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({"MSG":"Updated succefully"})
        return Response({"MSg":"Proper validation not enterd"})
    except:
        return Response({"MSg":"ID not found"})




# 1)GenericViewApi
# 2)3r party api
# 3)own api(creator)
#
#
# 2.5 -3 exp
#
# drf 1-1.5 yr
# @api_view()

# LLD HLD

# roles respolsibilites
# 1)api creation
# 2)database mangemnt
# 3)3rd party api integration





































