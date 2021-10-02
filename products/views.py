from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import (
    Product, Gender, Category, SubCategory, ArticleType, SpecialOffer)


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    products = Product.objects.all()
    sort = None
    direction = None
    query = None
    gender = None
    category = None
    sub_category = None
    article_type = None
    special_offer = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'gender' in request.GET:
            gender = request.GET['gender'].split(',')
            products = products.filter(
                gender__name__in=gender)
            gender = Gender.objects.filter(
                name__in=gender)

        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(
                category__name__in=category)
            category = Category.objects.filter(
                name__in=category)

        if 'sub_category' in request.GET:
            sub_category = request.GET['sub_category'].split(',')
            products = products.filter(
                sub_category__name__in=sub_category)
            sub_category = SubCategory.objects.filter(
                name__in=sub_category)

        if 'article_type' in request.GET:
            article_type = request.GET['article_type'].split(',')
            products = products.filter(
                article_type__name__in=article_type)
            article_type = ArticleType.objects.filter(
                name__in=article_type)

        if 'special_offer' in request.GET:
            special_offer = request.GET['special_offer'].split(',')
            products = products.filter(
                special_offer__name__in=special_offer)
            special_offer = SpecialOffer.objects.filter(
                name__in=special_offer)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria")
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) |
                Q(product_description__icontains=query) |
                Q(gender__name__icontains=query) |
                Q(category__name__icontains=query) |
                Q(sub_category__name__icontains=query) |
                Q(article_type__name__icontains=query) |
                Q(special_offer__name__icontains=query))
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'search_term': query,
        'current_gender': gender,
        'current_category': category,
        'current_sub_category': sub_category,
        'current_article_type': article_type,
        'current_special_offer': special_offer,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)
