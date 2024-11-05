from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from app_comment.serializers import CommentSerializer
from app_comment.models import CommentModel


class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.all()
    permission_classes = [IsAuthenticated]
