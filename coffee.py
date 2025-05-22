class Coffee:
    def __init__(self, name):
        # Validate name (string, at least 3 characters)
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    def orders(self):
        # Return a list of Order instances for this coffee
        from order import Order
        return [order for order in Order._all_orders if order.coffee == self]

    def customers(self):
        # Return a unique list of Customer instances who ordered this coffee
        return list(set(order.customer for order in self.orders()))