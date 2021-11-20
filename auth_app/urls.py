from django.urls import path

from .views import LoginView, ManualLoginView, LoginCustomView, CheckToken
from auth_app import views

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('manual/', ManualLoginView.as_view()),
    path('custom/', LoginCustomView.as_view()),
    path('check-token/', CheckToken.as_view()),

    path('create_product/', views.ProductCreateView.as_view()),
    path('update_product/<int:pk>/', views.ProductUpdateView.as_view()),
    path('delete_product/<int:pk>/', views.ProductDeleteView.as_view()),
    path('detail_product/<int:pk>/', views.ProductDetailView.as_view()),
    path('detail_all_products/<int:pk>/', views.ProductAllDetailView.as_view()),

]
