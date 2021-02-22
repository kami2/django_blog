from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:content_id>/', views.single, name='single')
]