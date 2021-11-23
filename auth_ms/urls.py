"""auth_ms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from auth_app.views.usuarios import CrearUsuarioView, DetalleUsuarioView
from auth_app.views import producCreateView,productAllDetailView,productDeleteView,productUpdateView,productDetailView
from auth_app.views import userCreate,userDetail,userAllDetail,userUpdate,userDelete

urlpatterns = [
    path('usuario/', CrearUsuarioView.as_view(), name='usuarios'),
    path('usuario/<int:pk>', DetalleUsuarioView.as_view(), name='usuario'),
    path('manual/', include('auth_app.urls')),
    path('simple/', include('auth_app.urls_simple_jwt')),

    
    path('create_product/', producCreateView.ProductCreateView.as_view()),
    path('update_product/<int:pk>/', productUpdateView.ProductUpdateView.as_view()),
    path('delete_product/<int:pk>/', productDeleteView.ProductDeleteView.as_view()),
    path('detail_product/<int:pk>/', productDetailView.ProductDetailView.as_view()),
    path('detail_all_products/<int:pk>/', productAllDetailView.ProductAllDetailView.as_view()),

    path('create_user/',userCreate.UserCreate.as_view()),
    path('detail_user/<int:pk>/',userDetail.UserDetail.as_view()),
    path('detail_all_user/<int:pk>/',userAllDetail.UserAllDetail.as_view()),
    path('update_user/<int:pk>/', userUpdate.UserUpdate.as_view()),
    path('delete_user/<int:pk>/', userDelete.UserDelete.as_view()),
]
# re_path() url basadas en expresiones regulares
