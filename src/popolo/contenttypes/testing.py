# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import popolo.contenttypes


class PopoloContenttypesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=popolo.contenttypes)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'popolo.contenttypes:default')


POPOLO_CONTENTTYPES_FIXTURE = PopoloContenttypesLayer()


POPOLO_CONTENTTYPES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(POPOLO_CONTENTTYPES_FIXTURE,),
    name='PopoloContenttypesLayer:IntegrationTesting',
)


POPOLO_CONTENTTYPES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(POPOLO_CONTENTTYPES_FIXTURE,),
    name='PopoloContenttypesLayer:FunctionalTesting',
)


POPOLO_CONTENTTYPES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        POPOLO_CONTENTTYPES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PopoloContenttypesLayer:AcceptanceTesting',
)
