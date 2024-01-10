from django.test import TestCase
from resturant.models import CustomUser
from resturant.factories.user_factory import CustomUserFactory


class UserTestModel(TestCase):

    def test_user_display_name(self):
        user = CustomUserFactory()
        excepted_display_name = 'Maheen_Butt123'
        self.assertEqual(excepted_display_name,user.display_name)
    
    def test_user_email(self):
        user = CustomUserFactory()
        excepted_email = f'{user.email}'
        self.assertEqual(excepted_email,user.email)