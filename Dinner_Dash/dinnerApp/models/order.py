from django.db import models

from .custom_user import CustomUser
from .item import Item


class Order(models.Model):
    STATUS_CHOICES = [
        ('ordered', 'Ordered'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
        ('done', 'Done')
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ordered')
    date_placed = models.DateTimeField(auto_now_add=True)
    in_process = models.BooleanField(default=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    orderIems = models.ManyToManyField(Item, through='OrderItem')

    def __str__(self):
        return f"Order #{self.pk} - {self.status}"

    class Meta:
        ordering = ['date_placed']