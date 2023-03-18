from django.urls import path
from .views import CustomUserViewSet

app_name = 'users'
urlpatterns = [
    path('', CustomUserViewSet.as_view()),
]