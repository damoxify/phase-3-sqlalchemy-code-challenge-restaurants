# Restaurant Review using SQLAlchemy

This is a Python application that uses SQLAlchemy to manage restaurant reviews. The application consists of three main models: `Restaurant`, `Customer`, and `Review`. These models are connected by relationships that allow for easy access to reviews, customers, and restaurants. The app provides various methods and functionalities for managing restaurant reviews.

## Prerequisites

Before using this application, ensure you have the following prerequisites:

- Python installed on your system.
- SQLAlchemy library installed. You can install it using pip: `pip install SQLAlchemy`.

## Getting Started

1. Clone or download the application code from the repository.
2. Open a terminal or command prompt and navigate to the application directory.

## Database Setup

The application uses SQLite as its database. You can set up the database by running the following commands:

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a database engine
engine = create_engine('sqlite:///restaurants.db', echo=True)

# Create tables
Base = declarative_base()
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
```

## Model Descriptions

### Restaurant

- Represents a restaurant with attributes like `name` and `price`.
- Has a one-to-many relationship with `Review` and a many-to-many relationship with `Customer`.
- Provides methods to retrieve all reviews and customers associated with the restaurant.
- Includes a class method `fanciest()` to find the restaurant with the highest price.

### Customer

- Represents a customer with attributes like `first_name` and `last_name`.
- Has a many-to-many relationship with `Restaurant` and a one-to-many relationship with `Review`.
- Provides methods to retrieve all reviews and restaurants associated with the customer.
- Includes methods to retrieve the customer's full name, favorite restaurant, add a review, and delete reviews for a specific restaurant.

### Review

- Represents a review with a `rating` attribute.
- Belongs to a `Restaurant` and a `Customer`.
- Provides a method to format the review as a string.

## Object Relationship Methods

### Review

- `customer()`: Returns the `Customer` instance for this review.
- `restaurant()`: Returns the `Restaurant` instance for this review.

### Restaurant

- `reviews()`: Returns a collection of all the reviews for the `Restaurant`.
- `customers()`: Returns a collection of all the customers who reviewed the `Restaurant`.

### Customer

- `reviews()`: Returns a collection of all the reviews that the `Customer` has left.
- `restaurants()`: Returns a collection of all the restaurants that the `Customer` has reviewed.

## Aggregate and Relationship Methods

### Customer

- `full_name()`: Returns the full name of the customer, with the first name and last name concatenated Western style.
- `favorite_restaurant()`: Returns the restaurant instance that has the highest star rating from this customer.
- `add_review(restaurant, rating)`: Takes a `restaurant` (an instance of the `Restaurant` class) and a rating, and creates a new review for the restaurant with the given `restaurant_id`.
- `delete_reviews(restaurant)`: Takes a `restaurant` (an instance of the `Restaurant` class) and removes all their reviews for this restaurant.

### Review

- `full_review()`: Returns a string formatted as follows: "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars."

### Restaurant

- `fanciest() (class method)`: Returns one restaurant instance for the restaurant that has the highest price.

## Testing the Methods

To test the methods and functionalities of the application, you can create sample instances of `Restaurant`, `Customer`, and `Review` and use the provided methods. Make sure to add and commit these instances to the session for testing.

## Usage

You can use this application to manage restaurant reviews, find the fanciest restaurant, and retrieve customer information. Explore the provided methods to see how they can help you manage and analyze restaurant reviews.

Please note that this readme provides an overview of the application's functionality and usage. Detailed code implementation can be found in the code files provided.

Enjoy using the Restaurant Review App!