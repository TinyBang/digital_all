from mod.base_handler import BaseHandler
from databases.tables import User
from sqlalchemy.orm.exc import NoResultFound
from cache.cache import cache
import tornado.web
import IPython


class SignInHandler(BaseHandler):
    def post(self):
        ret_code = {
            'code':100,'content':'ok'
        }
        user_name = self.get_argument('username',default=False)
        user_password=self.get_argument('userpassword',default=False)
        if not user_password or not user_password:
            ret_code['code']=201
            ret_code['content']=u'用户名密码不能为空'
        else:
            try:
                user=self.db.query(User).filter(User.username==user_name).one()
                if user.userpassword!=user_password:
                    ret_code['code']=202
                    ret_code['content']=u'密码错误'
                if user.userpassword==user_password:
                    if not self.get_secure_cookie("key"):
                        self.set_secure_cookie("key",str(user.id))
                        print("set cookie")
                    else:
                        print("cookie exists")
                cache.update([(str(user.id),user_name)])
            except NoResultFound as e:
                ret_code['code']=203
                ret_code['content']=u'账号不存在'
            except:
                ret_code['code']=204
                ret_code['content']=u'系统错误，登陆失败，请稍后再试'
        self.write_back(ret_code)