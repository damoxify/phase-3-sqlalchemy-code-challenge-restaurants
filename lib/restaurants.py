from sqlalchemy import String, Integer, ForeignKey, Column, create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    price = Column(Integer)

    reviews = relationship('Review', backref='restaurant')
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')
        
    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()


    def all_reviews(self):
        review_list = []

        for review in self.reviews:
            name_of_customer = f"{review.customer.first_name} {review.customer.last_name}"
            string_review = f"Review for {self.name} by {name_of_customer}: {review.rating} stars. "

            review_list.append(string_review)

        return review_list





class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Review', backref='customer')
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def favorite_restaurant(self):
        favorite_restaurant = None
        for review in self.reviews:
            if review.rating > max_rating:
                max_rating = review.rating
                favorite_restaurant = review.restaurant
        return favorite_restaurant


    def add_review(self, restaurant, rating):  
        review = Review(restaurant=restaurant, star_rating=rating)
        session.add(review)
        session.commit()    

    def delete_reviews(restaurant):
        delete_reviews = []

        for review in delete_reviews:
            if review.restaurant == restaurant:
                delete_reviews.append(review)

        for review in delete_reviews:
            session.delete(review)
            session.commit()





class Review(Base):
    __tablename__ ='reviews'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id')) 

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.full_name()}: {self.rating} stars"



engine = create_engine('sqlite:///restaurants.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session= Session()


# Customer
customer1 = Customer(first_name='Ade', last_name='Ayo')
session.add(customer1)
session.commit()


# Restaurant
# restaurant1 = Restaurant(name="KFC Chicken", price=100)
restaurant2 = Restaurant(name="Sweet sensation", price=50)
restaurant3 = Restaurant(name="Mr Biggs", price=200)
restaurant4 = Restaurant(name="Dominos", price=400)
restaurant5 = Restaurant(name="Dodo Pizza", price=250)

# session.add(restaurant1)
session.add(restaurant2)
session.add(restaurant3)
session.add(restaurant4)
session.add(restaurant5)

session.commit()




# TEST FOR OUR METHODS
#  CUSTOMERS
print(customer1.full_name())

# favorite = customer1.favorite_restaurant()
# print(f"{customer1.full_name()}'s favorite restaurant is {}")


# add_review
# customer1.add_review("KFC Chicken", 5)


# Restaurant 
fanciest = Restaurant.fanciest()
print(f"The fanciest restuarant is {fanciest.name}")