from django.db import models
from django.contrib.auth import (get_user_model)

User = get_user_model()
# Create your models here.


class Question(models.Model):
    """
    This is the Question Model it handles all the questions.
    """
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
