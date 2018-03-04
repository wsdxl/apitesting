import unittest
import requests
from ddt import ddt, data, unpack


from library.getData import get_xls_data


@ddt
class APITesting(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

   
    @data(*get_xls_data('./data/post_data.xls'))
    @unpack
    def test_post_topic(self,token,title,tab,content,except_statuscode):
        url = 'http://118.31.19.120:3000/api/v1/topics'
        post_data={
            "accesstoken":token,
            "title":title,
            "tab":tab,
            "content":content
        }
        res = requests.post(url,post_data)
        assert res.status_code == except_statuscode

    def tearDown(self):
       pass

    @classmethod
    def tearDownClass(self):
        pass
