from urlparse import urlparse
from urllib import unquote
from collective.picnik import edit
from collective.picnik.tests import base
from collective.picnik.tests import utils

class UnitTest(base.UnitTestCase):
    def setUp(self):
        super(UnitTest,self).setUp()
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
        self.failUnless(url.startswith('http://www.picnik.com/service/?'))
        parsed = urlparse(url)
        query = unquote(parsed.query)
        self.failUnless('_apikey=my_api_key' in query, query)
        self.failUnless('_import=http://localhost:8080/Plone/myimage' in query)
        self.failUnless('_export=http://localhost:8080/Plone/myimage/@@picnik_pull_handler' in query)
        self.failUnless('_export_agent=browser' in query)

class IntegrationTest(base.IntegrationTestCase):
    def test_call(self):
        pass
    
    def test_http_get_edit(self):
        pass
    
    def test_api_key(self):
        pass

