
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Home', 'Home'),
        ('Books', 'Books'),
        ('Other', 'Other'),
    ]
    GRADE_CHOICES = [
        ('New', 'New'),
        ('Average', 'Average'),
        ('Poor', 'Poor'),
    ]

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    grade = models.CharField(max_length=20, choices=GRADE_CHOICES)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
