"""
class definition of a State and an instance Base = declarative_base():
"""

# Start link class to table in database

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
'''
A base class that serves as the foundation for defining
databse models(tables) using the ORM approach
'''


class State(Base):
    '''
    This is a model class which inherits from Base class
    It defines attributes and relationships between tables
    The __tablename__ variable specifies what will appear
    when you print out this object
    In other words it's the name of our table in the DB
    Atrributes:
        id - unique identity number for each state
        name - state name (string), max length=128 chars
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Create engine and connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the table
    Base.metadata.create_all(engine)
