# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from politikus.popolo.testing import POLITIKUS_POPOLO_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

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

    def test_types_installed(self):
        """Test that all politikus.popolo content types are installed."""
        portal_types = api.portal.get_tool('portal_types')
        names = (
            'Area',
            'Contact Detail',
            'Identifier',
            'Membership',
            'Organization',
            'Other Name',
            'Person',
            'Post',
            'Relationship',
            'Source',
        )
        for name in names:
            fti = portal_types.getTypeInfo(name)
            self.assertIsNotNone(
                fti,
                'Content type {0} is not installed'.format(name),
            )

    def test_catalog_indexes_installed(self):
        """Test that the politikus.popolo catalog indexes are installed."""
        catalog = api.portal.get_tool('portal_catalog')
        indexes = (
            ('start_date', 'DateIndex'),
            ('end_date', 'DateIndex'),
            ('founding_date', 'DateIndex'),
            ('dissolution_date', 'DateIndex'),
            ('classification', 'FieldIndex'),
            ('gender', 'FieldIndex'),
        )
        for name, meta_type in indexes:
            self.assertIn(name, catalog.indexes())
            index = catalog._catalog.indexes[name]
            self.assertEqual(index.meta_type, meta_type)

    def test_catalog_columns_installed(self):
        """Test that the politikus.popolo catalog meta columns are installed."""
        catalog = api.portal.get_tool('portal_catalog')
        names = (
            'start_date',
            'end_date',
            'founding_date',
            'dissolution_date',
            'classification',
            'gender',
        )
        for name in names:
            self.assertIn(name, catalog.schema())

    def test_registry_records_installed(self):
        """Test that the politikus.popolo querystring registry records are installed."""
        registry = getUtility(IRegistry)
        for prefix, title in (
            ('start_date', 'Start Date'),
            ('end_date', 'End Date'),
            ('founding_date', 'Founding Date'),
            ('dissolution_date', 'Dissolution Date'),
        ):
            record = 'plone.app.querystring.field.{}'.format(prefix)
            self.assertTrue(registry['{}.enabled'.format(record)])
            self.assertEqual(registry['{}.title'.format(record)], title)
            self.assertTrue(registry['{}.sortable'.format(record)])

    def test_permissions_installed(self):
        """Test that the politikus.popolo add permissions are granted to Contributor."""
        granted = [
            item['name']
            for item in self.portal.permissionsOfRole('Contributor')
            if item['selected']
        ]
        names = (
            'politikus.popolo: Add Relationship',
            'politikus.popolo: Add Source',
            'politikus.popolo: Add Area',
            'politikus.popolo: Add Identifier',
            'politikus.popolo: Add OtherName',
            'politikus.popolo: Add ContactDetail',
            'politikus.popolo: Add Post',
            'politikus.popolo: Add Membership',
            'politikus.popolo: Add Organization',
            'politikus.popolo: Add Person',
        )
        for name in names:
            self.assertIn(name, granted)

    def test_vocabulary_factories_installed(self):
        """Test that the politikus.popolo vocabulary factories are registered."""
        from zope.schema.interfaces import IVocabularyFactory
        for name in (
            'politikus.popolo.relationshiptypes',
            'politikus.popolo.geonamefeaturecodes',
            'politikus.popolo.organizationcategories',
        ):
            self.assertIsNotNone(
                getUtility(IVocabularyFactory, name),
                'Vocabulary factory {0} is not registered'.format(name),
            )

    def test_uninstall_profile_hidden(self):
        """Test that the uninstall profile is hidden from the quick installer."""
        from plone.base.interfaces import INonInstallable
        adapter = getUtility(INonInstallable, name='politikus.popolo')
        self.assertIn(
            'politikus.popolo:uninstall',
            adapter.getNonInstallableProfiles(),
        )


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

    def test_types_removed(self):
        """Test that the politikus.popolo content types are removed."""
        portal_types = api.portal.get_tool('portal_types')
        names = (
            'Area',
            'Contact Detail',
            'Identifier',
            'Membership',
            'Organization',
            'Other Name',
            'Person',
            'Post',
            'Relationship',
            'Source',
        )
        for name in names:
            self.assertIsNone(portal_types.getTypeInfo(name))

    def test_catalog_indexes_removed(self):
        """Test that the politikus.popolo catalog indexes are removed."""
        catalog = api.portal.get_tool('portal_catalog')
        names = (
            'start_date',
            'end_date',
            'founding_date',
            'dissolution_date',
            'classification',
            'gender',
        )
        for name in names:
            self.assertNotIn(name, catalog.indexes())

    def test_catalog_columns_removed(self):
        """Test that the politikus.popolo catalog columns are removed."""
        catalog = api.portal.get_tool('portal_catalog')
        names = (
            'start_date',
            'end_date',
            'founding_date',
            'dissolution_date',
            'classification',
            'gender',
        )
        for name in names:
            self.assertNotIn(name, catalog.schema())

    def test_registry_records_removed(self):
        """Test that the politikus.popolo registry records are removed."""
        registry = getUtility(IRegistry)
        prefixes = (
            'start_date',
            'end_date',
            'founding_date',
            'dissolution_date',
        )
        for prefix in prefixes:
            leftovers = [
                record for record in registry.records
                if record.startswith(
                    'plone.app.querystring.field.{}'.format(prefix))
            ]
            self.assertEqual(leftovers, [])

    def test_permissions_reset(self):
        """Test that the local politikus.popolo permission grants reset."""
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        granted = [
            item['name']
            for item in self.portal.permissionsOfRole('Contributor')
            if item['selected']
        ]
        setRoles(self.portal, TEST_USER_ID, roles_before)
        self.assertNotIn('politikus.popolo: Add Person', granted)
