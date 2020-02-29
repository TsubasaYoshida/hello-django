from django.db import models

class Brand(models.Model):
    """ブランド"""
    class Meta:
        db_table = 'brand'

    code = models.CharField(
        'ブランドコード',
        max_length=64,
        unique=True,
    )
    name = models.CharField(
        'ブランド名',
        max_length=64,
    )
    created_at = models.DateTimeField(
        '作成日時',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        '更新日時',
        auto_now=True,
    )

    def __str__(self):
        return self.code

class Product(models.Model):
    """品番"""
    class Meta:
        db_table = 'product'
        default_related_name = 'products'
        unique_together = ('brand', 'code')

    brand = models.ForeignKey(
        Brand,
        verbose_name='ブランドコード',
        on_delete=models.CASCADE,
    )
    code = models.CharField(
        '品番',
        max_length=64,
    )
    created_at = models.DateTimeField(
        '作成日時',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        '更新日時',
        auto_now=True,
    )
        
    def __str__(self):
        return self.code

class Sku(models.Model):
    """SKU"""
    class Meta:
        db_table = 'sku'
        default_related_name = 'skus'
        unique_together = ('brand', 'code')

    code = models.CharField(
        'SKU',
        max_length=64,
    )
    brand = models.ForeignKey(
        Brand,
        verbose_name='ブランドコード',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        verbose_name='品番',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        '作成日時',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        '更新日時',
        auto_now=True,
    )

    def __str__(self):
        return self.code
