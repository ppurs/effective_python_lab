from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from topics.models import Topic

@admin.register(Topic)
class TopicAdmin(MPTTModelAdmin):
    list_display = ['title' ,'public']
    list_editable = ['public']


