from django.urls import path
from topics.views import TopicListView, TopicDetailView, TopicCreateView, TopicDeleteView, TopicUpdateView, add_topic_note
# from notes.views import NoteCreateView

urlpatterns = [
    path('', TopicListView.as_view(), name='topic-list'),
    path('add/', TopicCreateView.as_view(), name='topic-add'),
    path('<slug:slug>/', TopicDetailView.as_view(), name='topic-detail'),
    path('<slug:slug>/update', TopicUpdateView.as_view(), name='topic-update'),
    path('<slug:slug>/delete/', TopicDeleteView.as_view(), name='topic-delete'),
    path('<slug:slug>/add-note/', add_topic_note, name='add-topic-note')
]