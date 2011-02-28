from plone.testing import z2

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting

class Layer(PloneSandboxLayer):
    default_bases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.picnik
        self.loadZCML(package=collective.picnik)

        # Install product and call its initialize() function
        z2.installProduct(app, 'collective.picnik')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'collective.picnik:default')

    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, 'collective.picnik')

FIXTURE = Layer()

INTEGRATION = IntegrationTesting(bases=(FIXTURE,), name="Picnik:Integration")
FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,), name="Picnik:Functional")
