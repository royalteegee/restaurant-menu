import sys
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# This models the database and it's structure
class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    location = Column(String(500), nullable=False) # added a new column called location


class MenuItem(Base):
    __tablename__ = 'menu_item'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    status = Column(String, default='Available 🟢')
    description = Column(String(250))
    price = Column(String)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
