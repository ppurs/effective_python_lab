from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from django.urls import reverse
from topics.models import Topic


class Note(TimeStampedModel, models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='note_created_by')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("note-detail", kwargs={"pk": self.pk})