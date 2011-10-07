from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from collective.picnik.interfaces import PicnikConfiguration
from plone.z3cform import layout

class PanelForm(RegistryEditForm):
    schema = PicnikConfiguration

ControlPanelView = layout.wrap_form(PanelForm,
                                    ControlPanelFormWrapper)
ControlPanelView.label = u"Picnik settings"
