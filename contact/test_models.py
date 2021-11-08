from django.test import TestCase
from contact.models import Contact


class TestContactModels(TestCase):

    def test_contact_model(self):
        contact = Contact.objects.create(
            query_title='Hallo',
            query_text='Test Text',
            query_email='test@test.com',
        )
