import datetime
from bdayreminder.db.base import DBSession
from bdayreminder.db.models import Person


session = DBSession()
person1 = Person(
    name='John',
    dob=datetime.datetime.now().date(),
    email='saluasif@gmail.com',
    mobile=9916016104
)

session.add(person1)

person2 = Person(
    name='Jane',
    dob=datetime.datetime.now().date(),
    email='noreplycse@gmail.com',
    mobile=9916016103
)

session.add(person2)
session.commit()
session.close()
