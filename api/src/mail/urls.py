from django.urls import path, include
from mail import views


urlpatterns = [
    path('mail/', views.MailView.as_view()),
]