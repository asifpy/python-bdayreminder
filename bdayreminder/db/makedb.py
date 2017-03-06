from bdayreminder.db.base import Base, engine
import bdayreminder.db.models


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
