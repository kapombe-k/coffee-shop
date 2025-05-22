# This file defines the Order class which connects the coffee and customer classes
# Orders are stored in a class level list as the SSOT

class Order:

    #This class attributes stores all order instances(SSOT)
    #This list is shared across all order objects and allows Customer and coffee to query orders
    
    _all_orders = []  # Class attribute to store all orders

    def __init__(self, customer, coffee, price):
        # Store customer, coffee, and price as instance attributes
        # Validate price (float between 1.0 and 10.0)
        if not isinstance(price, float) or price < 1.0 or price > 10.0:
            raise ValueError("Price must be a float between 1.0 and 10.0")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order._all_orders.append(self)  # Add this order to the class list

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price