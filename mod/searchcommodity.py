from mod.base_handler import BaseHandler
from databases.tables import Commodity
from sqlalchemy.orm.exc import NoResultFound
import IPython


class SearchCommodityHandler(BaseHandler):
    def post(self):
        item_name = self.get_argument('searchitem')

        ret_code={
            'code':0,
            'content':''
        }
        try:

            allresult=[]
            for item in self.db.query(Commodity).filter(Commodity.name==item_name):
                ret_code['code']=100
                result = {
                }

                piclink = []

                result['id'] = str(item.id)

                result['name'] = item.name
                result['sort'] = str(item.sort)
                result['intro'] = item.introduce
                if not item.piclink1 == None:
                    piclink.append(item.piclink1)
                if not item.piclink2 == None:
                    piclink.append(item.piclink2)
                if not item.piclink3 == None:
                    piclink.append(item.piclink3)
                if not item.piclink4 == None:
                    piclink.append(item.piclink4)
                if not item.piclink5 == None:
                    piclink.append(item.piclink5)
                if not item.piclink6 == None:
                    piclink.append(item.piclink6)
                if not item.piclink7 == None:
                    piclink.append(item.piclink7)
                if not item.piclink8 == None:
                    piclink.append(item.piclink8)
                if not item.piclink9 == None:
                    piclink.append(item.piclink9)
                result['piclinks'] = piclink
                allresult.append(result)
                #arrcommodityid.append(item.id)
                #arrcommodityname.append(item.id)
            ret_code['content']=allresult
           # ret_code={
           #     'content':arrcommodityid
               # arrcommodityname,
                #arrcommoditysort,
                #arrcommodityintro

            #}
        except:
            ret_code['code']=304
            ret_code['content']=u'系统错误，请稍后再试'
        self.write_back(ret_code)
