#!/usr/bin/python3
""" receiver module """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Receiver(Base):
    """ The receiver class, contains sender name, phone, cash, the_status """
    __tablename__ = 'receiver'

    name = Column(String(120), nullable=False)
    phone = Column(String(20), nullable=False)
    cash = Column(String(100), nullable=False)

    def print_dict(self):
        """ to print the dictionary """
        print(self.__dict__)

    def to_dict(self):
        """ convert class in a dictionary """
        return self.__dict__
