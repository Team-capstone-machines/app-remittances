#!/usr/bin/python3
""" history module """
import datetime
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class History(Base):
    """ The history class, contains shipment date, phone, balance """
    __tablename__ = 'history'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    phone = Column(String(20), nullable=False)
    balance = Column(String(100), nullable=False)

    def __init__(self, id, date):
        """ method constructor """
        self.id = id
        self.date = datetime.datetime.now()

    def print_dict(self):
        """ to print the dictionary """
        print(self.__dict__)

    def to_dict(self):
        """ convert class in a dictionary """
        return self.__dict__
