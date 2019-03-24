from django.db import models

from stackoverflow.apps.questions.models import Question
# Create your models here.


class Comment(models.Model):
    """
    This is the Comment model with all the fields
    """
    # id = models.AutoField(auto_created=True, primary_key=True)
    comment = models.TextField(blank=True)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE)
