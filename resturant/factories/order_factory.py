# order_factory.py
import factory
from resturant.models import Order, OrderItem, EXPORTED_STATUS_CHOICES
from resturant.factories.user_factory import CustomUserFactory

class OrderFactory(factory.Factory):
    class Meta:
        model = Order
    
    status = factory.Faker('random_element', elements=[choice[0] for choice in EXPORTED_STATUS_CHOICES])
    date_placed = factory.Faker('date_time_this_decade', before_now=True)
    in_process = factory.Faker('boolean')
    user = factory.SubFactory(CustomUserFactory)
    order_total = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)

    @factory.post_generation
    def order_items(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for item in extracted:
                OrderItem.objects.create(order=self, item=item, quantity=1, subtotal=item.price)
