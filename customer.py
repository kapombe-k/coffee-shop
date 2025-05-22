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
    
    def create_order(self, coffee, price):
        from order import Order #import happens here avoiding circulation
        # here we create a new order and then return it directly
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficianado(cls, coffee):
        # this will be the class method to find a customer who has spent most on x coffee
        from order import Order 
        # get all orders of given coffee
        coffee_orders = [order for order in Order._all_orders if order.coffee==coffee]

        if not coffee_orders:
            return None
        
        #make a dict to track spending per customer
        customer_spending={}
        for order in coffee_orders:
            customer=order.customer
            if customer in customer_spending:
                customer_spending[customer] += order.price
            else:
                customer_spending[customer]=order.price

        #Return the customer with the highest total spending
        return max(customer_spending, key=customer_spending.get)