#!/usr/bin/env python3
""" DB Class """

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """ DB class ORM with sqlalchemy """

    def __init__(self):
        """ constructor method """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ session method """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ self descriptive add_user
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        ''' self descriptive '''
        try:
            record = self._session.query(User).filter_by(**kwargs).first()
        except TypeError:
            raise InvalidRequestError
        if record is None:
            raise NoResultFound
        return record

    def update_user(self, user_id: int, **kwargs) -> None:
        '''self descriptive'''
        user_record = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if hasattr(user_record, key):
                setattr(user_record, key, value)
            else:
                raise ValueError

        self._session.commit()
