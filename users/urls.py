from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import LoginView, RegisterView, UserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user')

]