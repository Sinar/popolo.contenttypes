# -*- coding: utf-8 -*-
from popolo.contenttypes.content.identifier import IIdentifier  # NOQA E501
from popolo.contenttypes.testing import POPOLO_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class IdentifierIntegrationTest(unittest.TestCase):

    layer = POPOLO_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Person',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_identifier_schema(self):
        fti = queryUtility(IDexterityFTI, name='Identifier')
        schema = fti.lookupSchema()
        self.assertEqual(IIdentifier, schema)

    def test_ct_identifier_fti(self):
        fti = queryUtility(IDexterityFTI, name='Identifier')
        self.assertTrue(fti)

    def test_ct_identifier_factory(self):
        fti = queryUtility(IDexterityFTI, name='Identifier')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IIdentifier.providedBy(obj),
            u'IIdentifier not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_identifier_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Identifier',
            id='identifier',
        )

        self.assertTrue(
            IIdentifier.providedBy(obj),
            u'IIdentifier not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('identifier', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('identifier', parent.objectIds())

    def test_ct_identifier_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Identifier')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
