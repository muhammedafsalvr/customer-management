from django.urls import path, include,re_path
from events import views


app_name = "events"

urlpatterns = [
    path('create/', views.create_event, name="create_event"),
    path('edit/<uuid:pk>/', views.edit_event, name="edit_event"),
    
]
