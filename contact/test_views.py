from django.test import TestCase
from django.contrib.auth import get_user_model


class TestCheckoutViews(TestCase):
    """
    Tests the contact page redirects correctly
    """

    def test_profile_page(self):
        response = self.client.get('/contact', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(
            response, '/contact/', status_code=301, target_status_code=200)
