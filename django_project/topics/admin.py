from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from topics.models import Topic

@admin.register(Topic)
class TopicAdmin(MPTTModelAdmin):
    list_display = ['title' ,'public']
    list_editable = ['public']

    def has_change_permission(self, request, obj=None):  
        if obj:
            if request.user == obj.created_by:
                return True
            
        return False


