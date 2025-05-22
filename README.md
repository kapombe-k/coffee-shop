# Coffee Shop Domain Model

A Python-based Object-Oriented Programming (OOP) application to model a Coffee Shop domain with entities for Customer, Coffee, and Order. This project demonstrates key OOP principles such as encapsulation, relationships, and data validation.


This project is designed to model the operations of a Coffee Shop using Object-Oriented Programming (OOP) principles. It simulates real-world interactions between customers, coffee menu items, and orders. The main goal is to demonstrate an understanding of OOP concepts such as classes, instances, attributes, methods, encapsulation, and relationships (one-to-many and many-to-many) while maintaining a single source of truth for data.

The application consists of three core entities:

Customer: Represents a person who places orders at the coffee shop.
Coffee: Represents a type of coffee available on the menu.
Order: Represents a transaction linking a customer to a coffee with a specific price.
These entities are interconnected to model realistic relationships, such as a customer placing multiple orders for different coffees, and a coffee being ordered by multiple customers.

### Domain Model Design
The domain model was designed to reflect the relationships between the three main entities before any code was written. This step involved sketching a conceptual diagram to visualize how data flows and connects. Below is a textual representation of the relationships:

Customer ↔ Order (One-to-Many): A single customer can place many orders, but each order belongs to only one customer.
Coffee ↔ Order (One-to-Many): A single coffee can be associated with many orders, but each order is for only one coffee.
Customer ↔ Coffee (Many-to-Many via Order): A customer can order many coffees, and a coffee can be ordered by many customers, with the Order entity acting as the intermediary.
This design ensures that data integrity is maintained by avoiding duplication and enforcing a single source of truth through the Order class, which stores all order instances in a centralized list.

### Class Structure and Files
The project is organized into three Python files, each containing a class definition corresponding to one of the main entities. The files are modular to promote clarity and scalability:

customer.py: Defines the Customer class, which manages customer data (e.g., name) and provides methods to access related orders and coffees.
coffee.py: Defines the Coffee class, which handles coffee menu item data (e.g., name) and provides methods to access related orders and customers.
order.py: Defines the Order class, which links a customer to a coffee with a price and serves as the central repository for all order data using a class-level list (_all_orders).
This structure avoids circular import issues by importing dependencies within methods rather than at the top of files, ensuring the code runs without errors.

### Initializers and Properties
Each class includes an initializer (__init__) to set up instance attributes with proper validation, along with properties to control access to these attributes:

Customer Class (customer.py):
Initialized with a name (string, 1-15 characters). Validation ensures the input meets these criteria, raising a ValueError otherwise.
Provides a read-only name property to access the customer’s name.
Coffee Class (coffee.py):
Initialized with a name (string, at least 3 characters). Validation enforces the length requirement.
Provides a read-only name property to access the coffee’s name.
Order Class (order.py):
Initialized with a customer (instance of Customer), a coffee (instance of Coffee), and a price (float, 1.0-10.0). Validates that inputs are of the correct type and within acceptable ranges.
Provides read-only properties for customer, coffee, and price to prevent modification after creation, adhering to encapsulation principles.
These initializers and properties ensure data integrity from the moment an object is created.

### Object Relationship Methods
The classes implement methods to manage and query relationships between objects, reflecting the one-to-many and many-to-many connections:

Order Class (order.py):
customer property: Returns the associated Customer instance.
coffee property: Returns the associated Coffee instance.
Customer Class (customer.py):
orders(): Returns a list of all Order instances placed by this customer by querying the centralized order list.
coffees(): Returns a unique list of Coffee instances ordered by this customer, derived from their orders.
Coffee Class (coffee.py):
orders(): Returns a list of all Order instances for this coffee by querying the centralized order list.
customers(): Returns a unique list of Customer instances who have ordered this coffee, derived from its orders.
These methods dynamically retrieve related data without storing redundant information, maintaining a single source of truth in the Order class.

### Aggregate and Association Methods
Additional methods provide functionality to create associations and compute aggregate data:

Customer Class (customer.py):
create_order(coffee, price): Allows a customer to place a new order by creating an Order instance with the provided Coffee instance and price, linking it to this customer. Returns the new Order object for further use.
Coffee Class (coffee.py):
num_orders(): Returns the total number of orders for this coffee, calculated by counting associated orders.
average_price(): Returns the average price of all orders for this coffee. Returns 0.0 if no orders exist to prevent division by zero.
These methods enable practical operations like placing orders and analyzing order statistics, mirroring real-world coffee shop activities.

### Class Method Implementation
A class method is implemented in the Customer class to provide functionality not tied to a specific instance:

Customer Class (customer.py):
most_aficionado(coffee): A @classmethod that accepts a Coffee instance and returns the Customer who has spent the most money on that coffee. It iterates through all orders for the given coffee, sums the spending per customer, and identifies the top spender. Returns None if no orders exist for the coffee.
This method demonstrates the use of class-level operations to analyze data across all instances, a useful feature for business insights like identifying loyal customers.

