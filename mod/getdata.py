from mod.base_handler import BaseHandler
from databases.tables import Commodity
from databases.tables import User
from sqlalchemy.orm.exc import NoResultFound
import IPython


class GetDataHandler(BaseHandler):
    def post(self):
        ret_code = {
            'code': 0,
            'content': u'没有该类商品'
        }
        commoditysort=self.get_argument("sort")
        try:
            # IPython.embed()
            # items=self.db.query(Commodity).filter(Commodity.name==item_name).all()
            # IPython.embed()
            arrcommodityid = []
            arrcommodityname = []
            arrcommoditysort = []
            arrcommodityintro = []
            allresult = []
            for item in self.db.query(Commodity).filter(Commodity.sort == commoditysort):
                ret_code['code']=100
                result = []

                piclink = []

                result.append('id:' + str(item.id))

                result.append('name:' + item.name)

                result.append('intro:' + item.introduce)
                if not item.piclink1 == 'null':
                    piclink.append(item.piclink1)
                if not item.piclink2 == 'null':
                    piclink.append(item.piclink2)
                if not item.piclink3 == 'null':
                    piclink.append(item.piclink3)
                if not item.piclink4 == 'null':
                    piclink.append(item.piclink4)
                if not item.piclink5 == 'null':
                    piclink.append(item.piclink5)
                if not item.piclink6 == 'null':
                    piclink.append(item.piclink6)
                if not item.piclink7 == 'null':
                    piclink.append(item.piclink7)
                if not item.piclink8 == 'null':
                    piclink.append(item.piclink8)
                if not item.piclink9 == 'null':
                    piclink.append(item.piclink9)
                result.append(piclink)
                allresult.append(result)
                # arrcommodityid.append(item.id)
                # arrcommodityname.append(item.id)
            ret_code['content'] = allresult
            # ret_code={
            #     'content':arrcommodityid
            # arrcommodityname,
            # arrcommoditysort,
            # arrcommodityintro

            # }
        except:
            ret_code['code'] = 204
            ret_code['content'] = u'系统错误，请稍后再试'
        self.write_back(ret_code)
