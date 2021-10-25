#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from os import getenv

Base = declarative_base()


class Receiver(Base):
    """ The receiver class, contains sender name, phone, cash """
    __tablename__ = 'table_receiver'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False)
    phone = Column(String(40), nullable=False)
    cash = Column(String(100), nullable=False)

    def __init__(self, **kwargs):
        """ method constructor """
        if kwargs:
            print(kwargs)
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)


class History(Base):
    """ The history class, contains shipment date, phone, balance """
    __tablename__ = 'table_history'

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


class Phones(Base):
    """ The phones class, contains sender phone encrypted and decrypted """
    __tablename__ = 'table_phones'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    phone = Column(String(40), nullable=False)
    phone_desencrypt = Column(String(40), nullable=False)

    def __init__(self, **kwargs):
        """ method constructor """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)


classes = {
    "Receiver": Receiver,
    "History": History,
    "Phones": Phones
}


class DBstorage():
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            "mssql+pyodbc://remittances_user:DUXowU%$dBmB"
            "@remittances.database.windows.net:1433/"
            "remittances_db?driver=ODBC+Driver+17+for+SQL+Server")

    def all(self, cls=None):
        """Query on the current database session"""
        new_dict = {}
        if cls in classes:
            objs = self.__session.query(classes[cls]).all()
            print(objs)
            for obj in objs:
                key = obj.id
                new_dict[key] = obj
        return new_dict

    def get(self, cls, phone):
        """This method is to retrieve one object """
        list_objs = []
        for value in self.all(cls).values():
            if value.phone == phone:
                list_objs.append(value)
        return list_objs

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def update(self, cls, phone, cash):
        """Update the column payout"""
        self.__session.query(classes[cls]).filter(
            classes[cls].phone == phone).update({'cash': cash})
        self.save()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.remove()

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session


storage = DBstorage()
storage.reload()
