import unittest
from collective.picnik.tests import base

class UnitTest(unittest.TestCase):
    def test_call(self):
        pass
    
    def test_get_image_url(self):
        pass
    
    def test_fecth_image(self):
        pass
    
    def test_field(self):
        pass
    
class IntegrationTest(base.IntegrationTestCase):
    def test_call(self):
        pass

    def test_get_image_url(self):
        pass
    
    def test_fecth_image(self):
        pass
    
    def test_field(self):
        pass
    
    def test_update_context(self):
        pass

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(UnitTest))
    suite.addTest(unittest.makeSuite(IntegrationTest))
    return suite
