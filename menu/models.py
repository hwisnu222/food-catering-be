from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    VEGETARIAN = 'VG'
    VEGAN = 'VN'
    GLUTEN_FREE = 'GF'
    DIET_CHOICES = [
        (VEGETARIAN, 'Vegetarian'),
        (VEGAN, 'Vegan'),
        (GLUTEN_FREE, 'Gluten-Free'),
    ]

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    description = models.TextField()
    base_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    dietary_type = models.CharField(
        max_length=2,
        choices=DIET_CHOICES,
        blank=True
    )
    preparation_time = models.PositiveIntegerField(help_text="Dalam menit")
    is_available = models.BooleanField(default=True)
    image = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.category})"