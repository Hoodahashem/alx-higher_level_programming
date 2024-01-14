#!/usr/bin/python3

"""importing the needed modules!"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    qu = session.query(State).filter(State.name.like("%a%"))
    results = qu.all()
    for result in results:
        session.delete(result)
    session.commit()
    session.close()
