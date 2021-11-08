from django.test import TestCase
from contact.forms import ContactQuery


class TestContactForm(TestCase):

    def test_query_title_is_required(self):
        form = ContactQuery({
            'query_title': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('query_title', form.errors.keys())
        self.assertEqual(
            form.errors['query_title'][0], 'This field is required.')

    def test_query_text_is_required(self):
        form = ContactQuery({
            'query_text': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('query_text', form.errors.keys())
        self.assertEqual(
            form.errors['query_text'][0], 'This field is required.')

    def test_query_email_is_required(self):
        form = ContactQuery({
            'query_email': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('query_email', form.errors.keys())
        self.assertEqual(
            form.errors['query_email'][0], 'This field is required.')

    def test_form_fields(self):
        form = ContactQuery()
        fields = []
        for field in form.fields:
            fields.append(field)
            print(field)
        self.assertEqual(fields,
                         ['query_title', 'query_text', 'query_email'])
