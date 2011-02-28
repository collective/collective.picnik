from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from collective.picnik import config
from collective.picnik import logger
import urllib

class Edit(BrowserView):
    """Redirect to picnik editor"""

    def __call__(self, *args):
        islocalhost = self.request.URL.startswith('http://localhost')
        if self.request.method == 'GET' and not islocalhost:
            return self.http_get_edit()
        elif islocalhost:
            logger.info('doesn t support localhost editing at the moment')
            return 'localhost is not supported'

    def http_get_edit(self):
        """Use the http get picnik method.
        
        You must be warned it doesn't work with localhost
        """
        kwargs = {}
        context_url = self.context.absolute_url()
        kwargs['_apikey'] = self.api_key()
        kwargs['_import'] = context_url
        kwargs['_export'] = context_url + '/@@picnik_pull_handler'
        kwargs['_export_agent'] = 'browser'
        url = config.SERVICE_URL + '?' + urllib.urlencode(kwargs)
        logger.info(kwargs)
        self.request.response.redirect(url)
        return ''

    def api_key(self):
        pp = getToolByName(self.context, 'portal_properties')
        api_key = pp.picnik_properties.apikey
        if not api_key:
            logger.error('You must provide an api key first')
        return api_key
