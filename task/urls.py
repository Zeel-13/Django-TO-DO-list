from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('update/<id>/',update,name="update"),
    path('delete/<id>/',delete,name="delete")
]


