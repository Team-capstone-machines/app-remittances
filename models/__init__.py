#!/usr/bin/python3
""" The storage variable is Initialized in the model's package.
"""

from models.engine.dbstorage import DBstorage

storage = DBstorage()
storage.reload()
