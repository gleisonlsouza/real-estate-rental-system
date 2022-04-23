
from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    # This function test if home view is correct
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home:home_index'))

        self.assertEqual(response.status_code, 200)

    def test_home_load_template(self):
        response = self.client.get(reverse('home:home_index'))

        self.assertTemplateUsed(response, 'home/pages/home.html')
