from collective.picnik import handle_pull
from collective.picnik.tests import base
from collective.picnik.tests import utils

URL = 'http://www.picnik.com/show/id/9549783515_wxnf9/imgVjCU/thumb320'

class UnitTest(base.UnitTestCase):
    def setUp(self):
        super(UnitTest,self).setUp()
        self.view = handle_pull.HandlePull(self.context, self.request)

    def test_call(self):
        def image_empty():
            return ''
        def image():
            return 'myimage'
        def update_context():
            pass
        self.view.fetch_image = image_empty
        self.view.update_context = update_context

        res = self.view()
        self.failUnless(res=="image fail to update")

        self.view.fetch_image = image
        res = self.view()
        self.failUnless(res=="image updated")

    def test_get_image_url(self):
        url = self.view.get_image_url()
        self.failUnless(not url)
        
        self.view.request.form['file'] = 'http://hurmpf.free.fr/img/13_luffy.jpg'
        url = self.view.get_image_url()
        self.failUnless(not url)
        
        self.view.request.form['file'] = URL
        url = self.view.get_image_url()
        self.failUnless(url == URL)

    def test_fecth_image(self):
        res = self.view.fetch_image()
        self.failUnless(not res)
        
        self.view.request.form['file'] = URL
        res = self.view.fetch_image()
        self.failUnless(res['mimetype']=='image/jpeg')
        self.failUnless(res['filename'].startswith("picnik_exported_image"))
        self.failUnless(res['filename'].endswith(".jpg"))
        self.failUnless(type(res['data'])==str)

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

