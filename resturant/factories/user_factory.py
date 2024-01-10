import factory
from resturant.models import CustomUser

class CustomUserFactory(factory.Factory):
    class Meta:
        model = CustomUser

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda o: f'{o.username}@example.com')
    display_name = 'Maheen_Butt123'
    password = factory.PostGenerationMethodCall('set_password', 'password123')
    