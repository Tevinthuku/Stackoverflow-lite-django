from rest_framework import generics
from rest_framework import permissions

from .models import Comment
from .serializers import CommentSerializer
# Create your views here.


class CommentsView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
