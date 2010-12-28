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
            return
        # Save the image
        self.update_image_field(image_data)

    def get_image_url(self):
        #Make sure we've been sent an image url
        image_url = self.request.form.get('file', None)
        if not image_url:
            logger.error("No image url has been provide")
            return
        # Make sure that the image came from picnik.  We don't want anyone
        # sending us data we didn't ask for!
        if not image_url.startswith("http://www.picnik.com"):
            logger.error("Sorry, the image URL doesn't seem right.")
            return
        return image_url

    def fetch_image(self):
        url = self.get_image_url()
        return urllib.urlopen(url)

    def update_image_field(self, data):
        filename = "picnik_exported_image" + datetime.now().isoformat()+ ".jpg"
        mimetype = 'image/jpeg'
        sio = StringIO()
        sio.write(image_data)
        field = self.context.getField('image') or self.context.getPrimaryField()
        field.set(
            self.context,
            image_data,
            mimetype=mimetype,
            filename=filename, 
            refresh_exif=False
        )
