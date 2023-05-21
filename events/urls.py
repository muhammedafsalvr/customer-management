from django.urls import path, include,re_path
from events import views


app_name = "events"

urlpatterns = [
    path('create/', views.create_event, name="create_event"),
     path('my_events/', views.my_events, name='my_events'),
    path('edit/<uuid:pk>/', views.edit_event, name="edit_event"),
    path('delete/<uuid:pk>/', views.delete_event, name='delete_event'),
    path('detail-event/<uuid:pk>/', views.detail_event, name='detail_event'),
    
    
    
]
