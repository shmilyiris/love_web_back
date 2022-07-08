from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
    path('event-view/', views.EventView.as_view(), name="event_view"),
    path('event-edit/<int:pk>/', views.EventEditView.as_view(), "event_edit"),
]
