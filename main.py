import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from sqlalchemy.orm import scoped_session, sessionmaker
from tornado.options import define, options
from mod.signup import SignUpHandler
from mod.signin import SignInHandler
from mod.getuserinfo import GetUserInfo
from mod.searchcommodity import SearchCommodityHandler
from mod.getdata import GetDataHandler
from mod.addcommodity import AddCommodityHandler
from mod.getcommoditybyid import GetCommodityById
from mod.start import StartHandler
from databases.db import engine

define("port", default=9999, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
         #   (r'/', IndexHandler),
            (r'/start', StartHandler),
            (r'/herald/.*', PageNotFoundHandler),
            (r'/signup',SignUpHandler),
            (r'/signin',SignInHandler),
            (r'/getuserinfo',GetUserInfo),
            (r'/searchcommodity',SearchCommodityHandler),
            (r'/getdata',GetDataHandler),
            (r'/addcommodity',AddCommodityHandler),
            (r'/searchbyid',GetCommodityById)
            ]
        settings = dict(
            cookie_secret='fdsafasdfasd',
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True,
            autoload=True,
            # autoescape=None
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = scoped_session(sessionmaker(bind=engine,
                                              autocommit=False, autoflush=True,
                                              expire_on_commit=False))


class PageNotFoundHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('404.html')
    def post(self):
        self.render('404.html')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    Application().listen(options.port)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()
