#!/usr/bin/python3
""" Module that contains the class DBStorage """

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.receiver import Receiver, Base
from models.history import History
from models.phones import Phones
""" from os import getenv """

classes = {
    "Receiver": Receiver,
    "History": History,
    "Phones": Phones
}

class DBstorage():
    __engine = None
    __session = None

    def __init__(self):
        _USER = 'gcnrjznlgzwtoa'
        _PWD = 'fffcd4f3290533a73019d0cab5ed80356ffd957b78d7b5f06145d588a2aa9164'
        _HOST = 'ec2-52-204-213-254.compute-1.amazonaws.com'
        _API_PORT = '5432'
        _DB = 'd131cd0p5meg7e'
        self.__engine = create_engine('postgres://{}:{}@{}:{}/{}'.
                                    format(_USER,
                                            _PWD,
                                            _HOST,
                                            _API_PORT,
                                            _DB))

    def all(self, cls=None):
        """Query on the current database session"""
        new_dict = {}
        if str(cls) in classes:
            objs = self.__session.query(classes[cls]).all()
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
