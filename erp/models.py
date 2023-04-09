from django.db import models
from accounts.models import UserModel
from decimal import Decimal

# 상품 : 상품코드, 상품명, 상품설명, 사이즈, 등록유저, 가격


class Product(models.Model):

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    code = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)
    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    
    class Meta:
        db_table = "product"

    def __str__(self):
        return self.code

# 입고 : 상품명(fk), 개수, 입고일자, 입고금액


class Inbound(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    inbound_quantity = models.IntegerField()
    inbound_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    class Meta:
        db_table = "inbound"

    def __str__(self):
        return self.product

    def save(self, *args, **kwargs):
        self.product.quantity += int(self.inbound_quantity)
        self.amount = Decimal(self.product.price) * Decimal(self.inbound_quantity)
        self.product.save()
        super().save(*args, **kwargs)
# 출고 : 상품명(fk), 개수, 출고일자, 출고금액


class Outbound(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    outbound_quantity = models.IntegerField()
    outbound_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    class Meta:
        db_table = "outbound"

    def __str__(self):
        return self.product

    def save(self, *args, **kwargs):
        self.product.quantity -= int(self.outbound_quantity)
        self.amount = Decimal(self.product.price) * Decimal(self.outbound_quantity)
        self.product.save()
        super().save(*args, **kwargs)
