import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bdayreminder.settings import DATABASE

# Create an engine that stores data in the local directory's
# db file.
detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
engine = create_engine(
    'sqlite:///{}'.format(DATABASE),
    connect_args={'detect_types': detect_types},
    native_datetime=True
)

Base = declarative_base()

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
