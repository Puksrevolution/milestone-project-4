"""
Code adapted from https://github.com/auxfuse/Milestone4
"""

from django import forms
from .models import Contact


class ContactQuery(forms.ModelForm):
    """
    Contact form with html attributes set via widgets handlers
    for same.
    """
    class Meta:
        model = Contact
        fields = [
            'query_title',
            'query_text',
            'query_email'
        ]

    query_title = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-group, form-control',
            'placeholder': 'Title'
        })
    )
    query_text = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Message'
        })
    )
    query_email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )
