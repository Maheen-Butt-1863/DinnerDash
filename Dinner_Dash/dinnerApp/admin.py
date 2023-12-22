from django.contrib import admin

# from .models.category import Category
from .models.custom_user import CustomUser
from .models.category import Category
from .models.item import Item
from .models.order import Order
from .models.orderitem import OrderItem

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(Item)