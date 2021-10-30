#!/usr/bin/python3
""" history module """
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class History(Base):
    """ The history class, contains shipment date, phone, balance """
    __tablename__ = 'history'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False, default=datetime.now())
    phone = Column(String(40), nullable=False)
    balance = Column(String(100), nullable=False)

    def __init__(self, **kwargs):
        """ method constructor """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.date = datetime.now()
        else:
            self.date = datetime.now()

    def print_dict(self):
        """ to print the dictionary """
        print(self.__dict__)

    def to_dict(self):
        """ convert class in a dictionary """
        return self.__dict__
