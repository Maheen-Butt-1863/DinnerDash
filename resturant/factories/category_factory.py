import factory
from resturant.models import Category

class CategoryFactory(factory.Factory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f'Category-{n}')