from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display =( 'id', 'title', 'created_date', 'published_date', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    
    

