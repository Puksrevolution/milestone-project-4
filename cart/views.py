# Code adapted from the CI Boutique Ado mini project


from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """
    This view returns the shopping cart contents page
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add the item & quantity to the shopping cart
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Store the shopping cart in the HTTP session
    cart = request.session.get('cart', {})

    """
    If a product with sizes is being added to the cart, then:
        if the same product id & size already exists, increase the quantity
        if the same product id exists, but has a new size, add the quantity
        Otherwise, add the new item and size to the cart
    Otherwise, add the product without a size to the cart
    """
    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    (
                        f'Updated size {size.upper()} {product.name} '
                        f'quantity to {cart[item_id]["items_by_size"][size]}'
                    )
                )
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    (
                        f'Added size {size.upper()} {product.name} '
                        f'to your cart'
                    )
                )
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                (
                    f'Added size {size.upper()} {product.name} to your cart'
                )
            )
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
                request,
                (
                    f'Updated {product.name} quantity to {cart[item_id]}'
                )
            )

        else:
            cart[item_id] = quantity
            messages.success(
                request,
                (
                    f'{product.name} has been added to your cart'
                )
            )

    request.session['cart'] = cart    
    return redirect(redirect_url)
