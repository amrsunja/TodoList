from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index_url'),
    path('update_task/<str:pk>', updateTask, name='update_url'),
    path('delete/<str:pk>', delete, name='delete_url'),

]