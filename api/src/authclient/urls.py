from django.urls import path, include
from authclient import views


urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('email-login/', views.TwoFactorLogin.as_view(), name='email-login')
]
