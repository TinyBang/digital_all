#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Date   : April 08, 2017
@Author : corvo
vim: set ts=4 sw=4 tw=99 et:
"""

from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from databases.db import Base


class Proj(Base):
    __tablename__ = 'proj'
    id = Column(Integer, primary_key=True)
    classify = Column(String(255))
    level = Column(String(255))
    intro = Column(String(10240))
    limits = Column(String(255))
    mail = Column(String(80))
    name = Column(String(50))
    phone = Column(String(20))
    start = Column(DateTime)
    status = Column(Integer)
    end = Column(DateTime)
    teacher = Column(String(20))



class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    username=Column(String(20))