from django.urls import path
from notes.views import NoteListView, NoteDetailView, NoteCreateView, NoteDeleteView, NoteUpdateView

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('add/', NoteCreateView.as_view(), name='note-add'),
    path('<int:pk>/update', NoteUpdateView.as_view(), name='note-update'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]