from mod.base_handler import BaseHandler
from databases.tables import User
from sqlalchemy.orm.exc import NoResultFound
import IPython


class GetUserInfo(BaseHandler):
    def post(self):
        user_name = self.get_argument('username')
        try:
            #IPython.embed()
            user=self.db.query(User).filter(User.username==user_name).one()
            ret_code={
                'userid':user.id,
                'name':user.username,
                'password':user.userpassword
            }
        except:
            ret_code['code']=104
            ret_code['content']=u'系统错误，请稍后再试'
        self.write_back(ret_code)
