import factory
from factory.django import DjangoModelFactory
from resturant.models import OrderItem

from .item_factory import ItemFactory
from .order_factory import OrderFactory


class OrderItemFactory(DjangoModelFactory):
    class Meta:
        model = OrderItem

    order = factory.SubFactory(OrderFactory)
    item = factory.SubFactory(ItemFactory)
    quantity = 1
