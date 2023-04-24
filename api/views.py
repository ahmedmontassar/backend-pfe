from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from .models import MyObject

def my_object_list(request):
    my_objects = [
        MyObject(1, 'object1', 'description1'),
        MyObject(2, 'object2', 'description2'),
        MyObject(3, 'object3', 'description3'),
    ]
    data = {'objects': my_objects}
    return JsonResponse(data)

# Create your views here.
