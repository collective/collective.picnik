from zope import component

from Products.CMFCore.utils import getToolByName
from plone.registry.interfaces import IRegistry

from collective.picnik import interfaces

def pass_(context):
    """One year after, I need to find what has changed between 1000 and 1001"""
    setup.runImportStepFromProfile(PROFILE, 'browserlayer')
    
def api_key_registry(context):
    """Move apikey from portal_properties to registry"""
    setup = getToolByName(context, 'portal_setup')

    #install registry step
    PROFILE = 'profile-collective.picnik:default'
    setup.runImportStepFromProfile(PROFILE, 'plone.app.registry')
    setup.runImportStepFromProfile(PROFILE, 'controlpanel')

    #get the api from portal_properties.picnik_properties
    pp = getToolByName(context, 'portal_properties')
    if 'picnik_properties' in pp:
        api = pp.picnik_properties.apikey
        if api:
            registry = component.queryUtility(IRegistry)
            configuration = registry.forInterface(interfaces.PicnikConfiguration)
            configuration.apikey = api

            pp._delObject('picnik_properties')
