from django.db import models

from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    skype = models.CharField(max_length=25)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def full_name(self):
        return "%s %s" % (self.name, self.surname)
