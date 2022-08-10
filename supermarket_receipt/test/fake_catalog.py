from catalog import SupermarketCatalog


class FakeCatalog(SupermarketCatalog):
    """A lightweight in-memory version of the SupermarketCatalog which would in reality be a database"""
    def __init__(self):
        self.products = {}
        self.prices = {}

    def add_product(self, product, price):
        self.products[product.name] = product
        self.prices[product.name] = price

    def unit_price(self, product):
        return self.prices[product.name]

