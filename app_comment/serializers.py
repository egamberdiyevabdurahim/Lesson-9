from rest_framework import serializers

from app_comment.models import CommentModel


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ['id', 'product', 'comment']
