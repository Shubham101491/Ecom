from django import template
register = template.Library()

@register.filter(name ='is_in_cart')
def is_in_cart(img , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == img.id:
            return True
    return False;
    
@register.filter(name ='cart_quantity')
def cart_quantity(img , cart):
    keys = cart.keys()
    for id in keys:
        # show error in id clear session no code changes
        if int(id) == img.id:
            return cart.get(id)
    return 0;

@register.filter(name ='price_total')
def price_total(img , cart):
    return int(str(img.watch_price)) * cart_quantity(img , cart)
    # ex return int(str(num) * 3) 
    
@register.filter(name ='total_price')
def total_price(products , cart):
    sum = 0;
    for p in products:
        sum += price_total(p , cart)
    return sum