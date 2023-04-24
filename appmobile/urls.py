from django.urls import path
from .views import MyObjectList

urlpatterns = [
    path('myobjects/', MyObjectList.as_view()),
]
