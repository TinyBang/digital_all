from mod.base_handler import BaseHandler
import tornado.web


class StartHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        ret_code = {
                'code': 100,
                'content': 'ok'
        }
        ret_code['content']=self.user
        self.write_back(ret_code)

    @tornado.web.authenticated
    def post(self):
        ret_code = {
                'code': 100,
                'content': 'ok'
        }
        ret_code['content']=self.user
        self.write_back(ret_code)

