from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from stackoverflow.apps.core.permissions import IsOwnerOrReadOnly
from .pagination import QuestionsPagination

from .models import Question
from .renderers import BaseRenderer
from .serializers import (QuestionsSerializer, SingleQuestionSerializer)
# Create your views here.


class QuestionsView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = QuestionsSerializer
    pagination_class = QuestionsPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'description', 'author__username')
    ordering_fields = ('title', 'author__username')
    renderer_classes = (BaseRenderer,)
    queryset = Question.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class SingleQuestionView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsOwnerOrReadOnly]
    serializer_class = SingleQuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'

    def get(self, request, id, *args, **kwargs):
        """Retrieve a single question"""
        question = get_object_or_404(Question, id=self.kwargs["id"])
        serializer = self.serializer_class(question)
        return Response(data={"data": serializer.data, "status": 200},
                        status=200)
