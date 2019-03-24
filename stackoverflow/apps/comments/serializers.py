from rest_framework import serializers

from .models import Comment
# from stackoverflow.apps.questions.serializers import QuestionsSerializer


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            "id",
            "question",
            "body"
        ]
