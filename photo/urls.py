from django.urls import path
from . import views

app_name = 'photo'

urlpatterns = [
    path('photo-view/', views.PhotoView.as_view(), name="photo_view"),
]
