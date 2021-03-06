"""
Code adapted from the CI Boutique Ado mini project
"""

from django import forms
from .widgets import CustomClearableFileInput
from .models import (
    Product, Gender, ArticleType, Category, SubCategory, SpecialOffer)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        gender = Gender.objects.all()
        article_type = ArticleType.objects.all()
        category = Category.objects.all()
        sub_category = SubCategory.objects.all()
        special_offer = SpecialOffer.objects.all()
        gender_display_name = [(
            g.id,
            g.gender_display_name()
        ) for g in gender]
        article_type_display_name = [(
            at.id,
            at.article_type_display_name()
        ) for at in article_type]
        category_display_name = [(
            c.id,
            c.category_display_name()
        ) for c in category]
        sub_category_display_name = [(
            sc.id,
            sc.sub_category_display_name()
        ) for sc in sub_category]
        special_offer_display_name = [(
            so.id,
            so.special_offer_display_name()
        ) for so in special_offer]

        self.fields['gender'].choices = gender_display_name
        self.fields['article_type'].choices = article_type_display_name
        self.fields['category'].choices = category_display_name
        self.fields['sub_category'].choices = sub_category_display_name
        self.fields['special_offer'].choices = special_offer_display_name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border rounded-0'
