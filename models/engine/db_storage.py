#!/usr/bin/python3
"""Module for DBStorage class."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Database storage engine for MySQL using SQLAlchemy."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage."""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_TYPE_STORAGE")

        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{pwd}@{host}/{db}",
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects of a given class from the database."""
        objects = {}
        classes = [State, City, User, Place, Review, Amenity]

        if cls:
            query_result = self.__session.query(cls).all()
        else:
            query_result = []
            for cls in classes:
                query_result.extend(self.__session.query(cls).all())

        for obj in query_result:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            objects[key] = obj

        return objects

    def new(self, obj):
        """Add new object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all database tables and initialize session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Call remove() method on the session."""
        self.__session.remove()

