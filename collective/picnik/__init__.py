  # -*- extra stuff goes here -*- 
import logging
logger = logging.getLogger('collective.picnik')

from zope.i18nmessageid import MessageFactory
messageFactory = MessageFactory("collective.picnik")

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
