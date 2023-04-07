from django.db import models
from accounts.models import UserModel

# 상품 : 상품코드, 상품명, 상품설명, 사이즈, 등록유저, 가격
class Product(models.Model):
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
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    price = models.CharField(max_length=256)
    quantity = models.IntegerField(default=0)
    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name

# 입고 : 상품명(fk), 개수, 입고일자, 입고금액
class Inbound(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    inbound_quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "inbound"

    def __str__(self):
        return self.code

# 출고 : 상품명(fk), 개수, 출고일자, 출고금액
class Outbound(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    outbound_quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "outbound"

    def __str__(self):
        return self.code
