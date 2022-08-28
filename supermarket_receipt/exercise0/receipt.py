
class ReceiptItem:
    def __init__(self, product, quantity, price, total_price):
        self.product = product
        self.quantity = quantity
        self.price = price
        self.total_price = total_price

    @property
    def quantity_type(self):
        return self.product.quantity_type


class WelcomeProduct:
    def __init__(self):
        self.name = "Welcome to Acme Supermarket!"
        self.unit = ""

class Receipt:
    def __init__(self):
        self._items = [ReceiptItem(WelcomeProduct(), 1, 0.00, 0.00)]
        self._discounts = []

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.total_price
        for discount in self.discounts:
            total -= discount.discount_amount
        return total

    def add_product(self, product, quantity, price, total_price):
        self._items.append(ReceiptItem(product, quantity, price, total_price))

    def add_discount(self, discount):
        self._discounts.append(discount)

    @property
    def items(self):
        return self._items[:]

    @property
    def discounts(self):
        return self._discounts[:]
