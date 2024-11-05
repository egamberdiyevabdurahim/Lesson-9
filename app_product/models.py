from django.db import models

from app_common.models import BaseModel


class ProductModel(BaseModel):
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.title}/{self.price}"