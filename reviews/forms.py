"""
Code adapted from https://github.com/BrianWhelanDublin/milestone-project-4
"""

from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = (
            'review',
            'stars'
        )
