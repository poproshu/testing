from django.urls import path, include
from customuser.views import PasswordChangeView, ProfileView


urlpatterns = [
    path('change-password/', PasswordChangeView.as_view()),
    path('profile/', ProfileView.as_view())
]