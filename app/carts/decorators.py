import functools

def update_cart_total(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        args[0].cart.save()
    return wrapper
