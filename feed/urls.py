from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
  
  path('',HomeView.as_view(),name='homeview'),

  path('dummydata/',DummyData,name='dummydata'),
  
  
  
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)