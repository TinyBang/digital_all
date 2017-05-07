from mod.base_handler import BaseHandler


class StartHandler(BaseHandler):

    def get(self):
        ret_code = {
                'code': 200,
                'content': 'ok'
        }
        self.write_back(ret_code)

    def post(self):
        ret_code = {
                'code': 200,
                'content': 'ok'
        }
        self.write_back(ret_code)

