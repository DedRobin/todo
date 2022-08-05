from django.contrib import admin
from notes.models import Note


@admin.register(Note)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "text", "created_at")
    fields = ("author", "title", "text", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "text")
