import factory

from resturant.constants import STATUS_CHOICES
from resturant.models import Order

from ..factories.user_factory import CustomUserFactory


class OrderFactory(factory.Factory):
    class Meta:
        model = Order

    status = factory.Faker('random_element', elements=[choice[0] for choice in STATUS_CHOICES])
    date_placed = factory.Faker('date_time_between', start_date='-7d', end_date='now')
    in_process = True
    user = factory.SubFactory(CustomUserFactory)
    order_total = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    