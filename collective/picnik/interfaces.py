from collective.picnik import logger
from zope import interface

#dependencies
try:
    #plone4
    from Products.ATContentTypes.interfaces.image import IATImage as IImage
except ImportError, e:
    logger.info('BBB: switch to plone3 %s'%e)
    #plone3
    from Products.ATContentTypes.interface import IATImage  as IImage

class IPicnikLayer(interface.Interface):
    """Browser layer for picnik addon"""
