from django.contrib import admin
from .models import Course, Lesson

admin.site.register(Course)
admin.site.register(Lesson)


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'short_description']
    inlines = [LessonInline, ]
