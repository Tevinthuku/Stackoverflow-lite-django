from rest_framework import generics
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .pagination import QuestionsPagination

from .models import Question
from .serializers import (QuestionsSerializer, SingleQuestionSerializer)
# Create your views here.


class QuestionsView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = QuestionsSerializer
    pagination_class = QuestionsPagination
    queryset = Question.objects.all()


class SingleQuestionView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SingleQuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'

    def get(self, request, id, *args, **kwargs):
        """Retrieve a single question"""
        question = get_object_or_404(Question, id=self.kwargs["id"])
        serializer = self.serializer_class(question)
        return Response(data={"data": serializer.data, "status": 200},
                        status=200)
