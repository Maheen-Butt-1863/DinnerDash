from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator
from django.db import models

from .category import Category


class Item(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    is_available = models.BooleanField(default=True)
    photo = CloudinaryField(
        "profile image",
        default="https://res.cloudinary.com/dqxbl0sux/image/upload/v1704364081/wqklk7lsghidaehjkrq0.png",
        blank=True,
        null=True,
    )
    categories = models.ManyToManyField(Category, related_name="items")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Item #{self.pk} - {self.title}"

    # def display_photo(self):
    #     if self.photo:
    #         return mark_safe(f'<img src="{self.photo.url}" width="50" height="50" />')
    #     return "No Photo"

    # display_photo.short_description = "Photo"
