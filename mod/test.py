from mod.base_handler import BaseHandler

class TestHandler(BaseHandler):

    def post(self):
        ret_code={
            'test':'ture'
        }
        self.write_back(ret_code)
