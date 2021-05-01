from django.urls import path, include
from customuser.views import PasswordChangeView


urlpatterns = [
    path('change-password/', PasswordChangeView.as_view()),
]