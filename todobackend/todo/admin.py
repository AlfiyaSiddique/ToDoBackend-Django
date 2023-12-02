from django.contrib import admin
from .models import Todo, Tag


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'dueDate', 'status')
    list_filter = ('status', 'dueDate')
    readonly_fields = ('timestamp',)  # Make timestamp readonly
    fieldsets = (
        ('Task Details', {
            'fields': ('title', 'description', 'dueDate', 'status')
        }),
        ('Tags', {
            'fields': ('tag',),
        }),
    )


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Todo, TodoAdmin)
admin.site.register(Tag, TagAdmin)

