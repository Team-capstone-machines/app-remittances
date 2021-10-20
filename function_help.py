#!/usr/bin/python3
""" Helper functions.
"""

import hashlib
import json
from os.path import exists


def Encrypt(number):
    """ This function adds the total cash.
    """
    pwd = number
    key = pwd.encode('utf-8')
    return hashlib.md5(key).hexdigest()


def Convert_int(number):
    """ This function convert to int.
    """
    if number.find('.') != -1:
        list_cash = number.split('.')
        return int(list_cash[0].replace(",", "").replace("$", ""))
    if number.find('+') != -1:
        return int(number.replace('+ ', ''))
    else:
        return int(number.replace('- ', ''))
