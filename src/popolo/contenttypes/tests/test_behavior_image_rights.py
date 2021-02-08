# -*- coding: utf-8 -*-
from popolo.contenttypes.behaviors.image_rights import IImageRightsMarker
from popolo.contenttypes.testing import POPOLO_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class ImageRightsIntegrationTest(unittest.TestCase):

    layer = POPOLO_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_image_rights(self):
        behavior = getUtility(IBehavior, 'popolo.contenttypes.image_rights')
        self.assertEqual(
            behavior.marker,
            IImageRightsMarker,
        )
