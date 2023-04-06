from django.db import models
from accounts.models import UserModel


class Product(models.Model):
    class Meta:
        db_table = "product"
    code = models.CharField(max_length=256)
    name = models.CharField(max_length=256)    
    description = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=256)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)
    def __str__(self):
        return self.name