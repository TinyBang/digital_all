#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Date   : April 09, 2017
@Author : corvo
vim: set ts=4 sw=4 tw=99 et:
"""

from cache.cache import cache
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

    def get_current_user(self):
        key = self.get_secure_cookie("key")
        ret_code = {
            'code': 000, 'content': '没有此用户的登陆数据'
        }
        if key:
            key = bytes.decode(key)
            if key in cache.keys():
                self.user=cache[key]
                self.user=cache[key]
                return cache[key]
            if key not in cache.keys():
                self.write_back(ret_code)
        else:
            return None