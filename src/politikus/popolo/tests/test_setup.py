# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from politikus.popolo.testing import POLITIKUS_POPOLO_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that politikus.popolo is properly installed."""

    layer = POLITIKUS_POPOLO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if politikus.popolo is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'politikus.popolo'))

    def test_browserlayer(self):
        """Test that IPolitikusPopoloLayer is registered."""
        from politikus.popolo.interfaces import (
            IPolitikusPopoloLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPolitikusPopoloLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = POLITIKUS_POPOLO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('politikus.popolo')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if politikus.popolo is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'politikus.popolo'))

    def test_browserlayer_removed(self):
        """Test that IPolitikusPopoloLayer is removed."""
        from politikus.popolo.interfaces import \
            IPolitikusPopoloLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPolitikusPopoloLayer,
            utils.registered_layers())
