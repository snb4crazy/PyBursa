from django.db import models


class Feedback(models.Model):

    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.subject
