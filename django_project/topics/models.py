from django.db import models
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from django.contrib.auth.models import User


class Topic(TitleSlugDescriptionModel, TimeStampedModel, MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    public = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_created_by')

    def get_absolute_url(self):
        return reverse("topic-detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']


        