from django.contrib import admin

from notes.models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):  
        if obj:
            if request.user == obj.created_by:
                return True
            
        return False

