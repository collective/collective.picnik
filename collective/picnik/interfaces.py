from collective.picnik import logger

#dependencies
try:
    #plone4
    from Products.ATContentTypes.interfaces.image import IATImage as IImage
except ImportError, e:
    logger.info('BBB: switch to plone3 %s'%e)
    #plone3
    from Products.ATContentTypes.interface import IATImage  as IImage
