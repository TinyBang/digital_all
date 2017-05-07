#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Date   : April 09, 2017
@Author : corvo
vim: set ts=4 sw=4 tw=99 et:
"""


import tornado.web
import json
from tornado.web import HTTPError



class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db

    def on_finish(self):
        self.db.close()

    def write_back(self, retjson):

        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(json.dumps(retjson, ensure_ascii=False, indent=2))
        self.finish()
