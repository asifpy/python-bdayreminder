from sqlalchemy.types import Integer, String, Date
from sqlalchemy import Column
from sqlalchemy.orm import validates
from bdayreminder.db.makedb import Base


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String, unique=True)
    dob = Column(Date)
    mobile = Column(Integer, unique=True)

    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address
        return address
