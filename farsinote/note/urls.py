from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:note_id>', views.detail, name='detail'),
    path('new/', views.new, name='new')
]
