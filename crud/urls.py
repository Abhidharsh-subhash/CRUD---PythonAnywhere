from django.urls import path
from .import views

urlpatterns = [
    path('',views.Product_crud.as_view(),name='Product_crud'),
]