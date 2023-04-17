from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.

@api_view(['GET'])
def get(request):
    model=Details.objects.all()
    serializer=DetailsSerializer(model,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def add(request):
    try:
        name=request.data['name']
        city=request.data['city']
        nameExist=Details.objects.filter(name=name).exists()
        if nameExist:
            return Response({"msg":"User already Exist"})
    
        model=Details.objects.create(name=name,city=city)
        model.save()
        serializer=DetailsSerializer(model)
        print(serializer.data)
        return Response({"Msg":"created successfully"})
    except Exception:
        return Response({"Msg":"Page not found...mising some data or invalid datatype"})
@api_view(['PUT'])
def update(request,id):
    try:
        name=request.data['name']
        city=request.data['city']
        userExist=Details.objects.filter(name=name).exists()
        if userExist:
            return Response({"Msg":"User alredy exist"})
        obj=Details.objects.get(id=id)
        obj.name=name
        obj.city=city
        obj.save()
        serializer=DetailsSerializer(obj,many=True)
        print(serializer)
        return Response({"Msg":"Updated Successfully"})
    except Exception:
        return Response({"Msg":"Page not found..missing some data or invalid datatype"})

@api_view(['DELETE'])
def delete(request,id):
    userExist=Details.objects.filter(id=id).exists()
    if userExist:
        model=Details.objects.get(id=id)
        model.delete()
        return Response({"Msg":"Deleted succesfully"})
    else:
        return Response({"Msg":"User not found with this id "})