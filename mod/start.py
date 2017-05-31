from mod.base_handler import BaseHandler
import tornado.web


class StartHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        ret_code = {
                'code': 100,
                'content': 'ok'
        }
        print(self.user)
        #self.get_current_user(self)
        ret_code['content']=self.user
        self.write_back(ret_code)


    def post(self):
        ret_code = {
                'code': 200,
                'content': 'ok'
        }
        self.write_back(ret_code)

