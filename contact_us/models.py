from django.db import models

# Create your models here.
class ContactUsSubmission(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200)
    comment = models.TextField()
    question_response = models.TextField()


class Reply(models.Model):
    comment = models.TextField()
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200)
