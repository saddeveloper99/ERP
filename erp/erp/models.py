from django.db import models
from accounts.models import UserModel

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=256)
    name = models.CharField(max_length=256)    
    description = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=256)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        # 생성될 때 stock quantity를 0으로 초기화 로직
        pass