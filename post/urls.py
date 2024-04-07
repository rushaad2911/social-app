from django.urls import path
from .views import *

urlpatterns = [

    path('<uuid:pk>/delete/',DeletePostView.as_view(),name='deletepostview'),
    path('create/',CreatePostView.as_view(),name='createpostview'),
    path('<uuid:pk>/',DetailPostView.as_view(),name='detailpostview'),
  
]
