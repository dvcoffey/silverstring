from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that renders the shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    gauge = None
    if 'string_gauge' in request.POST:
        gauge = request.POST['string_gauge']
    cart = request.session.get('cart', {})

    if gauge:
        if item_id in list(cart.keys()):
            if gauge in cart[item_id]['items_by_cart'].keys():
                cart[item_id]['items_by_gauge'][gauge] += quantity
                messages.success(request, f'Updated gauge {gauge.upper()} {Product.name} quantity to {cart[item_id]["items_by_gauge"][gauge]}')
            else:
                cart[item_id]['items_by_gauge'][gauge] = quantity
                messages.success(request, f'Added gauge {gauge.upper()} {Product.name} to your cart')
        else:
            cart[item_id] = {'items_by_gauge': {gauge: quantity}}
            messages.success(request, f'Added gauge {gauge.upper()} {Product.name} to your cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {Product.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {Product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the items in the cart"""

    quantity = int(request.POST.get('quantity'))
    gauge = None
    if 'string_gauge' in request.POST:
        gauge = request.POST['string_gauge']
    cart = request.session.get('cart', {})

    if gauge:
        if quantity > 0:
            cart[item_id]['items_by_gauge'][gauge] = quantity
        else:
            del cart[item_id]['items_by_size'][gauge]
            if not cart[item_id]['items_by_gauge']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {Product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {Product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the cart"""

    try:
        gauge = None
        if 'string_gauge' in request.POST:
            gauge = request.POST['string_gauge']
        cart = request.session.get('cart', {})

        if gauge:
            del cart[item_id]['items_by_gauge'][gauge]
            if not cart[item_id]['items_by_gauge']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {Product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
