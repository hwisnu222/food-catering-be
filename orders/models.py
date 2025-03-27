from django.db import models
from menu.models import MenuItem
import random
import string

# Create your models here.
class Order(models.Model):
    PENDING = 'P'
    CONFIRMED = 'C'
    IN_PROGRESS = 'IP'
    OUT_FOR_DELIVERY = 'OD'
    COMPLETED = 'CP'
    CANCELLED = 'CN'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (IN_PROGRESS, 'In Progress'),
        (OUT_FOR_DELIVERY, 'Out for Delivery'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    ]

    name = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=13, null=True)
    tracking_code = models.CharField(max_length=8, unique=True, blank=True, null=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT, null=True)
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    delivery_date = models.DateTimeField()
    delivery_address = models.TextField()
    special_notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=PENDING
    )

    def save(self, *args, **kwargs):
        print("pre save")
        if not self.tracking_code:
            print("save")
            self.tracking_code = self.generate_random_code()
            super().save(*args, **kwargs)


    def generate_random_code(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def __str__(self):
        return f"Order #{self.id} - {self.name}"

