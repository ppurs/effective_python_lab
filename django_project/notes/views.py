from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from notes.models import Note
from topics.models import Topic


class NoteListView(ListView):
    model = Note

class NoteDetailView(DetailView):
    model = Note

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'body', 'topic']
    
    def get_initial(self):
        initial = super().get_initial()
        if self.request.session.get('topic', False):
            initial['topic'] = Topic.objects.get(slug=self.request.session['topic'])
            self.request.session['topic'] = None
        return initial

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class NoteUpdateView(UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'body', 'topic']

    def test_func(self):
        return self.request.user == self.get_object().created_by

class NoteDeleteView(UserPassesTestMixin, DeleteView):
    model = Note
    success_url ="/notes"

    def test_func(self):
        return self.request.user == self.get_object().created_by or self.request.user.is_superuser