import factory
from resturant.models import OrderItem
from .item_factory import ItemFactory
from .order_factory import OrderFactory

class OrderItemFactory(factory.Factory):
    class Meta:
        model = OrderItem

    order = factory.SubFactory(OrderFactory)
    item = factory.SubFactory(ItemFactory)
    quantity = 1
    subtotal = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    