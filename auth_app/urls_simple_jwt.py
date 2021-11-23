from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views.login_simple_jwt import TestView, CustomTokenObtainPairView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('login/custom-payload/', CustomTokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('check-token/', TestView.as_view())
]
