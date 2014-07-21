# -*- coding: utf-8 -*-

"""
This layer is the Test class base.

Check out all tests on this package:

./bin/test -s ploneconf2014.theme --list-tests
"""

from plone.testing.z2 import ZSERVER_FIXTURE, installProduct, uninstallProduct

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.testing import Layer
from zope.configuration import xmlconfig

class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):

        # Load ZCML
        import ploneconf2014.theme
        self.loadZCML(package=ploneconf2014.theme)
        xmlconfig.file(
            'configure.zcml',
            ploneconf2014.theme,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        installProduct(app, 'ploneconf2014.theme')

    def tearDownZope(self, app):
        # Uninstall products installed above
        uninstallProduct(app, 'ploneconf2014.theme')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        applyProfile(portal, 'ploneconf2014.theme:default')

FIXTURE = Fixture()

"""
We use this base for all the tests in this package. If necessary,
we can put common utility or setup code in here. This applies to unit 
test cases.
"""
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="ploneconf2014.theme:Integration"
)

"""
We use this for functional integration tests. Again, we can put basic 
common utility or setup code in here.
"""
ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(FIXTURE, ZSERVER_FIXTURE),
    name="ploneconf2014.theme:Acceptance"
)
