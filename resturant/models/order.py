from django.db import models

from resturant.constants import STATUS_CHOICES

from .custom_user import CustomUser
from .item import Item


class Order(models.Model):
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ordered")
    date_placed = models.DateTimeField(auto_now_add=True)
    in_process = models.BooleanField(default=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    order_items = models.ManyToManyField(Item, through="OrderItem")
    action_timestamp = models.DateTimeField(null=True, blank=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Order #{self.pk} - {self.status}"

    class Meta:
        ordering = ["date_placed"]

    @classmethod
    def get_cart(cls, user):
        cart, created = cls.objects.get_or_create(
            user=user, status="ordered", in_process=True
        )
        return cart

# EXPORTED_STATUS_CHOICES = STATUS_CHOICES