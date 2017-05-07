#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Date   : April 08, 2017
@Author : corvo
vim: set ts=4 sw=4 tw=99 et:
"""

from databases.db import engine, Base
from databases.tables import Proj

if __name__ == '__main__':
    Base.metadata.create_all(engine)  # create all of Class which belonged to Base Class
    print ("Create OK")
