import unittest
from collective.picnik import edit
from collective.picnik import config
from collective.picnik.tests import base
from collective.picnik.tests import utils

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.context = utils.FakeContext()
        self.request = utils.FakeRequest()
        self.view = edit.Edit(self.context, self.request)

    def test_call(self):
        res = self.view()
        self.failUnless(res=="localhost is not supported")
        
        def http_get_edit():
            return 'http_get_edit'
        self.view.http_get_edit = http_get_edit
        self.request.URL = 'http://www.mywebsite.com/myimage'
        res = self.view()
        self.failUnless(res=="http_get_edit")

    def test_http_get_edit(self):
        def api_key():
            return 'my_api_key'
        self.view.api_key = api_key
        self.view.http_get_edit()
        url = self.request.response._redirect
        self.failUnless(url.startswith(config.SERVICE_URL))
        import pdb;pdb.set_trace()

class IntegrationTest(base.IntegrationTestCase):
    def test_call(self):
        pass
    
    def test_http_get_edit(self):
        pass
    
    def test_api_key(self):
        pass

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(UnitTest))
    suite.addTest(unittest.makeSuite(IntegrationTest))
    return suite
