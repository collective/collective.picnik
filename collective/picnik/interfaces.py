from zope import interface
from zope import schema

from collective.picnik import logger, messageFactory as _
try:
    from Products.ATContentTypes.interfaces import IATImage as IImage
except ImportError, e:
    try:
        #plone4
        from Products.ATContentTypes.interfaces.image import IATImage as IImage
        logger.info('BBB: switch to plone4.0 %s'%e)
    except ImportError, e:
        logger.info('BBB: switch to plone3 %s'%e)
        #plone3
        from Products.ATContentTypes.interface import IATImage  as IImage


class IPicnikLayer(interface.Interface):
    """Browser layer for picnik addon"""

class PicnikConfiguration(interface.Interface):

    apikey = schema.ASCIILine(title=_(u"API KEY"),
                      description=_(u"You can create ask for an API KEY at \
                        https://www.picnik.com/keys/"),
                      default="")
