# factories.py
import factory
from factory.django import DjangoModelFactory

from ..models import Item


class ItemFactory(DjangoModelFactory):
    class Meta:
        model = Item

    title = factory.Sequence(lambda n: f"Item-{n}")
    description = "Item description"
    price = factory.Faker("pydecimal", left_digits=4, right_digits=2, positive=True)
    is_available = True

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if extracted:
            self.categories.set(extracted)
