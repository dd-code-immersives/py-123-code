# sqlalchemy_insert.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from sqlalchemy_declarative import Address, Base, Person  # The classes imported
 
engine = create_engine('sqlite:///sqlalchemy_CI.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
# 
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
 
# Insert a Person in the person table
new_person = Person(first_name='Jane', last_name = 'Reiss')
session.add(new_person)
session.commit()

 
# Insert an Address in the address table
new_address = Address(street_number= '11',
                    street_name='Washington ave',
                    post_code='99001', 
                    person=new_person)
session.add(new_address)
session.commit()