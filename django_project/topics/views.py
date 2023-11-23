from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from topics.models import Topic
from django.shortcuts import redirect
from django.urls import reverse


class TopicListView(ListView):
    model = Topic

class TopicDetailView(DetailView):
    model = Topic

class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'parent', 'public']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TopicUpdateView(UserPassesTestMixin, UpdateView):
    model = Topic
    fields = ['title', 'parent', 'public']

    def test_func(self):
        return self.request.user == self.get_object().created_by

class TopicDeleteView(UserPassesTestMixin, DeleteView):
    model = Topic
    success_url ="/topics"

    def test_func(self):
        return self.request.user == self.get_object().created_by or self.request.is_superuser
    

def add_topic_note(request, **kwargs):
    request.session['topic'] = kwargs['slug']
    return redirect(reverse('note-add'))
