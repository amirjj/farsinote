from django.urls import path
from .views import (
    NoteListView,
    NoteDetailView,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView
)

urlpatterns = [
    path('', NoteListView.as_view(), name='index'),
    path('create/', NoteCreateView.as_view(), name='create'),
    path('<int:pk>/', NoteDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', NoteUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='delete'),
    # path('new/', new, name='new')
]
