from django.db import models

# Create your models here.


class Question(models.Model):
    """
    This is the Question Model it handles all the questions.
    """
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
