# import the classes to test

from customer import Customer
from coffee import Coffee
from order import Order

# create some test data
customer1 = Customer("Eugene")
customer2 = Customer("Fiona")
coffee1 = Coffee('Latte')
coffee2 = Coffee('Espresso')

# create orders
order1= Order(customer1, coffee1, 4.5)
order2= Order(customer1, coffee2, 3.0)
order3= Order(customer2, coffee1, 5.0)

# test customer methods
print(f"{customer1.name}'s orders: {len(customer1.orders())}")  # Should be 2
print(f"{customer1.name}'s coffees: {[c.name for c in customer1.coffees()]}")  # Should be ['Latte', 'Espresso']

# Test Coffee methods
print(f"{coffee1.name} has {coffee1.num_orders()} orders")  # Should be 2
print(f"{coffee1.name}'s average price: {coffee1.average_price()}")  # Should be 4.75

# Test most_aficionado
top_customer = Customer.most_aficianado(coffee1)
print(f"Top spender on {coffee1.name}: {top_customer.name}")  # Should be Alice (spent $5.0)