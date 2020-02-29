from django.db import models

class Brand(models.Model):
    """ブランド"""
    created_at = models.DateTimeField(
        '作成日時',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        '更新日時',
        auto_now=True,
    )
    code = models.CharField(
        'ブランドコード',
        max_length=64,
        unique=True,
    )
    name = models.CharField(
        'ブランド名',
        max_length=64,
    )

    def __str__(self):
        return self.code

class Product(models.Model):
    """品番"""
    created_at = models.DateTimeField(
        '作成日時',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        '更新日時',
        auto_now=True,
    )
    brand = models.ForeignKey(
        Brand,
        verbose_name='ブランドコード',
        related_name='products',
        on_delete=models.CASCADE,
    )
    code = models.CharField(
        '品番',
        max_length=64,
    )

    class Meta:
        unique_together = ('brand', 'code')

    def __str__(self):
        return self.code

class Sku(models.Model):
    """SKU"""
    created_at = models.DateTimeField(
        '作成日時',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        '更新日時',
        auto_now=True,
    )
    code = models.CharField(
        'SKU',
        max_length=64,
    )
    brand = models.ForeignKey(
        Brand,
        verbose_name='ブランドコード',
        related_name='skus',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        verbose_name='品番',
        related_name='skus',
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('brand', 'code')

    def __str__(self):
        return self.code
