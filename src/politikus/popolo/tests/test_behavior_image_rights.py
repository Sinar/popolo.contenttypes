# -*- coding: utf-8 -*-
from politikus.popolo.behaviors.image_rights import IImageRightsMarker
from politikus.popolo.testing import POLITIKUS_POPOLO_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class ImageRightsIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_POPOLO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_image_rights(self):
        behavior = getUtility(IBehavior, 'politikus.popolo.image_rights')
        self.assertEqual(
            behavior.marker,
            IImageRightsMarker,
        )
