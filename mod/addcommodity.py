from mod.base_handler import BaseHandler
from databases.tables import Commodity
class AddCommodityHandler(BaseHandler):
    def post(self):
        ret_code = {
            'code': 100, 'content': '添加成功'
        }
        commodityname=self.get_argument("commodityname")
        commoditysort=self.get_argument("sort",default="0")
        commodityintro=self.get_argument("introduction",default='null')
        commoditypiclink1 = self.get_argument("piclink1")
        commoditypiclink2 = self.get_argument("piclink2")
        commoditypiclink3 = self.get_argument("piclink3")
        commoditypiclink4 = self.get_argument("piclink4")
        commoditypiclink5 = self.get_argument("piclink5")
        commoditypiclink6 = self.get_argument("piclink6")
        commoditypiclink7 = self.get_argument("piclink7")
        commoditypiclink8 = self.get_argument("piclink8")
        commoditypiclink9 = self.get_argument("piclink9")

        if not commodityname:
            ret_code['code'] = 101
            ret_code['content'] = u'商品名称不能为空'
        else:
            try:
                newcommodity = Commodity()
                newcommodity.name=commodityname
                newcommodity.sort=commoditysort
                newcommodity.introduce=commodityintro
                newcommodity.piclink1=commoditypiclink1
                newcommodity.piclink2 = commoditypiclink2
                newcommodity.piclink3 = commoditypiclink3
                newcommodity.piclink4 = commoditypiclink4
                newcommodity.piclink5 = commoditypiclink5
                newcommodity.piclink6 = commoditypiclink6
                newcommodity.piclink7 = commoditypiclink7
                newcommodity.piclink8 = commoditypiclink8
                newcommodity.piclink9 = commoditypiclink9
                self.db.add(newcommodity)
                self.db.commit()
            except:
                ret_code['code'] = 104
                ret_code['content'] = u'系统错误，添加商品失败，请稍后再试'
        self.write_back(ret_code)