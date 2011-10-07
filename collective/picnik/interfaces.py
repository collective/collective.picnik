from collective.picnik import logger
from zope import interface
from zope import schema
#dependencies
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

    apikey = schema.ASCIILine(title=u"API KEY", default="")
