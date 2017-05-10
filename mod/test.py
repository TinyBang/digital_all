from mod.base_handler import BaseHandler
from databases.tables import User
import IPython

class TestHandler(BaseHandler):

    def post(self):
        ret_code={
            'test':'ture'
        }
       # IPython.embed()
        user_name=self.get_argument('username',default='null')
        print('Done!')
        self.write_back('success')
        #username=User(username=user_name)
      #  print(self.db.query(User).fliter(User.username==user_name))
       # print(user_name)
        self.write_back(ret_code)
