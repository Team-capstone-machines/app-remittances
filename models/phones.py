#!/usr/bin/python3
""" phones module """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Phones(Base):
    """ The phones class, contains sender phone encrypted and decrypted """
    __tablename__ = 'phones'

    id = Column(Integer, nullable=False, autoincrement=True)
    phone = Column(String(40), ForeignKey('receiver.phone'), nullable=False)
    phone_decrypted = Column(String(40), nullable=False)

    def __init__(self, **kwargs):
        """ method constructor """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

    def print_dict(self):
        """ to print the dictionary """
        print(self.__dict__)

    def to_dict(self):
        """ convert class in a dictionary """
        return self.__dict__
