from django.contrib import admin
from .models import (
    Product, Gender, ArticleType, Category, SubCategory, SpecialOffer
)


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'sku',
                ('name', 'product_description', 'colour'),
                ('price', 'discount_price'),
                'image')
        }),
        ('Category Selections', {
            'classes': ('collapse',),
            'fields': (
                'gender',
                'category',
                'sub_category',
                'article_type',
                'special_offer'),
        }),
    )

    list_display = (
        'sku',
        'name',
        'product_description',
        'gender',
        'article_type',
        'colour',
        'price',
        'discount_price',
        'image'
    )


class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


class GenderAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(SpecialOffer, SpecialOfferAdmin)
