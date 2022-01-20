from django.urls import path, include
from .views import RegisterView
from . import views

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', views.login, name='login'),
]
