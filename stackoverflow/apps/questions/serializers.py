from rest_framework import serializers

from .models import Question
from stackoverflow.apps.comments.models import Comment
from stackoverflow.apps.comments.serializers import CommentSerializer


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            "id",
            "title",
            "description"
        ]


class SingleQuestionSerializer(serializers.ModelSerializer):
    comments_list = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Question
        fields = [
            "id",
            "title",
            "description",
            "comments_list"
        ]

    def get_comments_list(self, obj):
        qs = Comment.objects.filter(question=obj)
        return CommentSerializer(qs, many=True).data
