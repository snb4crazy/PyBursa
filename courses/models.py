from django.db import models
from coaches.models import Coach


class Course(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    coach = models.ForeignKey(Coach, null=True, blank=True, related_name='coach_courses')
    assistant = models.ForeignKey(Coach, null=True, blank=True, related_name='assistant_courses')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.subject

    def __str__(self):
        return self.subject

