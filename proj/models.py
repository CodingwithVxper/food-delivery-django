from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='restaurants')

    def __str__(self):
        return f"{self.name} cuisine is ({self.cuisine})."


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name}"


class MenuItem(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='menu_items', null=False)
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.item_name} - ${self.price}"


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='orders', null=False)
    order_date = models.DateTimeField(default=timezone.now, null=False)
    delivery_address = models.TextField()

    def __str__(self):
        return f"Order#{self.id} for {self.customer.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('order', 'item')

    def __str__(self):
        return f"{self.quantity} - {self.item.item_name} (Order #{self.order.id})"
