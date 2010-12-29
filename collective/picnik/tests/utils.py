class FakeResponse(object):
    def __init__(self):
        self._redirect = None
    def redirect(self, url):
        self._redirect = url

class FakeRequest(object):
    def __init__(self):
        self.response = FakeResponse()
        self.form = {}
        self.URL = 'http://localhost:8080/Plone'
        self.method = 'GET'

class FakeField:
    def __init__(self):
        self.value = None
    def get(self, context):
        return self.value
    def set(self, context, value):
        self.value = value

class FakeContext(object):
    def __init__(self):
        self.image = FakeField()
    
    def getField(self, name):
        if name == 'image':
            return self.image

    def absolute_url(self):
        return 'http://localhost:8080/Plone/myimage'
