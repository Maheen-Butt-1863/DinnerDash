import factory
from resturant.models import Item, Category

class ItemFactory(factory.Factory):
    class Meta:
        model = Item

    title = factory.Sequence(lambda n: f'Item-{n}')
    description = 'Item description'
    price = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    is_available = True

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.categories.add(category)
