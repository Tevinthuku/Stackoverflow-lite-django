from django.db import models
from django.contrib.auth import (get_user_model)

from stackoverflow.apps.questions.models import Question
User = get_user_model()
# Create your models here.


class Comment(models.Model):
    """
    This is the Comment model with all the fields
    """
    # id = models.AutoField(auto_created=True, primary_key=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
