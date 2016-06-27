from django.contrib import admin
from .models import Student


def fullname(obj):
    return "%s %s" % (obj.name, obj.surname)

fullname.short_description = 'full name'


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email', 'name']
    list_filter = ['courses']
    list_display = [fullname, 'email', 'skype']
    filter_horizontal = ('courses',)
    fieldsets = [
       ('Personal info', {'fields': ('name', 'surname', 'date_of_birth', )}),
       ('Contact info', {'fields': ('email', 'phone', 'address', 'skype', )}),
       (None, {'fields': ('courses', )})
    ]

admin.site.register(Student, StudentAdmin)
