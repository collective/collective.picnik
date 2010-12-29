import unittest
from collective.picnik.tests import base

class UnitTest(unittest.TestCase):
    def test_call(self):
        pass
    
    def test_http_get_edit(self):
        pass
    
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
