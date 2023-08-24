"""
Write a script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine and connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State object with letter a and order by id
    states = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    # Display the result if a state is found
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
