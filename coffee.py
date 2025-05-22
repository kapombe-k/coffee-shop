class Coffee:
    def __init__(self, name):
        # Validate name (string, at least 3 characters)
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters")
        self._name = name

    @property
    def name(self):
        # this getter method returns the coffee name as a string
        return self._name

    def orders(self):
        # Return a list of Order instances for this coffee
        from order import Order
        return [order for order in Order._all_orders if order.coffee == self]

    def customers(self):
        # Return a unique list of Customer instances who ordered this coffee
        return list(set(order.customer for order in self.orders()))
    
    def num_orders(self):
        #returns total orders for this coffee
        #uses the orders() method to get the count
        return len(self.orders())
    
    def average_price(self):
        #returns average price of all orders
        #0.0 is returned of no orders are provided

        orders = self.orders()
        if not orders:  #if no prders are provided return 0.0
            return 0.0
        
        # calculate the average 
        total_price = sum(order.price for order in orders)
        return total_price/len(orders)