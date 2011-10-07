from zope.event import notify
from Products.Archetypes.event import ObjectEditedEvent
from Products.Five import BrowserView
from collective.picnik import logger
import urllib
from datetime import datetime
from StringIO import StringIO


class HandlePull(BrowserView):
    """This is a controller to download image data from Picnik after we're given
       a temporary URL via HTTP GET.
    """
    
    def __call__(self, *args):
        # Download the image data from Picnik's servers
        image_data = self.fetch_image()
        if not image_data:
            # Download failed ... this shouldn't happen very often,
            # but you might want to put some retry logic in your app
            logger.error("Sorry, the image download failed.")
            return "image fail to update"
        # Save the image
        self.update_context()
        self.request.response.redirect(self.context.absolute_url()+'/view')

    def get_image_url(self):
        """Extract image url from the request and make some checks"""
        #Make sure we've been sent an image url
        image_url = self.request.form.get('file', None)
        if not image_url:
            logger.error("No image url has been provide")
            return ''
        # Make sure that the image came from picnik.  We don't want anyone
        # sending us data we didn't ask for!
        image_url = urllib.unquote(image_url)
        if not image_url.startswith("http://www.picnik.com") and not image_url.startswith("http://www.picnikr.com"):
            logger.error("Sorry, the image URL doesn't seem right: %s"%image_url)
            return ''
        return image_url

    def fetch_image(self):
        """download image and return dict object:
        {'filename': ... , 'data':..., 'mimetype':...}
        """
        url = self.get_image_url()
        if not url:
            return
        image = urllib.urlopen(url)
        if image.getcode() != 200:
            return
        res = {}
        res['filename'] = "picnik_exported_image" + datetime.now().isoformat()+ ".jpg"
        res['data'] = image.read()
        res['mimetype'] = image.info().gettype()

        return res

    def field(self):
        """Return the field supposed to be updated"""
        return self.context.getField('image') or self.context.getPrimaryField()

    def update_context(self):
        """Do the job to fetch image and update the context with it"""
        image_info = self.fetch_image()
        if not image_info:
            return "image download fails"
        sio = StringIO()
        sio.write(image_info['data'])
        field = self.field()
        field.set(
            self.context,
            image_info['data'],
            mimetype=image_info['mimetype'],
            filename=image_info['filename'], 
            refresh_exif=False
        )

        notify(ObjectEditedEvent(self.context))
