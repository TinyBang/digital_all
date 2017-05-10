from mod.base_handler import BaseHandler
from databases.tables import User
import IPython


class SignUpHandler(BaseHandler):
    def post(self):
        ret_code = {
            'test': 'ture'
        }
        #IPython.embed()
        user_name = self.get_argument('username', default='null')
        user_password=self.get_argument('userpassword',default='null')
        user=User(username=user_name,userpassword=user_password)
        print('Done!')
        self.write_back('success')
      #  self.db.add(user)

        # username=User(username=user_name)
        #  print(self.db.query(User).fliter(User.username==user_name))
        # print(user_name)
       # self.write_back(ret_code)
