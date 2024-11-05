from django.db import models
from django.contrib.auth import get_user_model

from app_common.models import BaseModel
from app_product.models import ProductModel

UserModel = get_user_model()


class CommentModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"{self.comment}/{self.user.username}"