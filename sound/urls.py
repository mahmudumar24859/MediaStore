from django.urls import path
from . import views

urlpatterns = [
    path('media', views.home, name='Home'),
    path('sahih_muslim_view', views.Sahih_Muslim_View, name='Sahih_Muslim_View'),
    path('upload_sahih_muslim', views.Sahih_Muslim_Upload,
         name='Sahih_Muslim_Upload'),
]
