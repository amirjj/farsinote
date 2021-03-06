from django.urls import path
from .views import NoteListView, NoteDetailView, NoteCreateView

urlpatterns = [
    path('', NoteListView.as_view(), name='index'),
    path('create/', NoteCreateView.as_view(), name='create'),
    path('<int:pk>/', NoteDetailView.as_view(), name='detail'),
    # path('new/', new, name='new')
]
