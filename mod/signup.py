from mod.base_handler import BaseHandler
from databases.tables import User
from sqlalchemy.orm.exc import NoResultFound
import IPython


class SignUpHandler(BaseHandler):
    def post(self):
        ret_code = {
            'code':100,'content':'注册成功'
        }

        user_name = self.get_argument('username',default=False)
        user_password=self.get_argument('userpassword',default=False)
        if not user_password or not user_password:
            ret_code['code']=101
            ret_code['content']=u'用户名密码不能为空'
            self.write_back(ret_code)
        else:
            try:
                user=self.db.query(User).filter(User.username==user_name).one()
                if user.username==user_name:
                    ret_code['code']=102
                    ret_code['content']=u'用户名已存在'
            except NoResultFound as e:
                newuser=User(username=user_name,userpassword=user_password)
                self.db.add(newuser)
                self.db.commit()
            except:
                ret_code['code']=104
                ret_code['content']=u'系统错误，注册失败，请稍后再试'
        self.write_back(ret_code)
