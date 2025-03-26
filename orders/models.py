from django.db import models
from django.contrib.auth.models import User
from menu.models import MenuItem

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

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    delivery_address = models.TextField()
    special_notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=PENDING
    )
    is_paid = models.BooleanField(default=False)

    @property
    def total_price(self):
        items_total = sum(item.price for item in self.items.all())
        return items_total + self.tax + self.delivery_fee

    def __str__(self):
        return f"Order #{self.id} - {self.user.email}"

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    special_request = models.TextField(blank=True)

    @property
    def price(self):
        addons_price = sum(addon.price for addon in self.selected_addons.all())
        return (self.menu_item.base_price + addons_price) * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.menu_item.name} (Order #{self.order.id})"