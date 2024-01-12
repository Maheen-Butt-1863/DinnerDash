from django.test import TestCase
from django.urls import reverse

from resturant.models import Category

from ..factories.category_factory import CategoryFactory


class CategoryPageViewTest(TestCase):

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/category/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('category'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('category'))
        print("status code",resp.status_code)
        self.assertTemplateUsed(resp, 'add_category.html')

    def test_create_category_success_test(self):
        self.assertEqual(Category.objects.count(), 0)
        new_category = CategoryFactory()
        url = reverse('category')
        form_data = {'name': new_category.name}
        response = self.client.post(url, form_data)
        self.assertEqual(Category.objects.count(), 1)
        category = Category.objects.first()
        self.assertEqual(category.name, new_category.name)

    def test_create_category_empty_field_test(self):
        self.assertEqual(Category.objects.count(), 0)
        url = reverse('category')
        form_data = {'name': ''}
        response = self.client.post(url, form_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())
        self.assertContains(response, 'This field is required.')
        self.assertEqual(Category.objects.count(), 0)