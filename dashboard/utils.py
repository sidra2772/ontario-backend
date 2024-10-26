import random
import string
from dashboard.models import Orders


def get_order_number():
    s = 10  # number of characters in the string.
    order_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=s))
    if Orders.objects.filter(order_number=order_number).exists():
        get_order_number()
    return order_number
