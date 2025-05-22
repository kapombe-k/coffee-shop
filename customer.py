# Customer class is defined here to represent the person making an order
# methods in this class manage orders and coffees associated with the customer

class Customer:
    def __init__(self, name):
        # Validate name (string between 1 and 15 characters)
        if not isinstance(name, str) or len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be a string between 1 and 15 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    def orders(self):
        # Returns a list of Order instances for this customer
        from order import Order  # Import here to avoid circular imports
        return [order for order in Order._all_orders if order.customer == self]

    def coffees(self):
        # Returns a unique list of Coffee instances this customer has ordered
        return list(set(order.coffee for order in self.orders()))