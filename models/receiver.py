#!/usr/bin/python3
""" receiver module """
from models.phones import Phones
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Receiver(Base):
    """ The receiver class, contains sender name, phone, cash """
    __tablename__ = 'receiver'

    id = Column(Integer, nullable=False, autoincrement=True)
    name = Column(String(120), nullable=False)
    phone = Column(String(40), nullable=False, primary_key=True)
    cash = Column(String(100), nullable=False)

    def __init__(self, **kwargs):
        """ method constructor """
        if kwargs:
            print(kwargs)
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

    def print_dict(self):
        """ to print the dictionary """
        print(self.__dict__)

    def to_dict(self):
        """ convert class in a dictionary """
        return self.__dict__
