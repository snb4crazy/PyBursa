from django.contrib import admin
from .models import Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    """
        Admin View for Course
    """
    search_fields = ['name']
    list_display = ['name', 'short_description']
    inlines = [LessonInline, ]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
