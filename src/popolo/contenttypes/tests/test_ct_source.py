# -*- coding: utf-8 -*-
from popolo.contenttypes.content.source import ISource  # NOQA E501
from popolo.contenttypes.testing import POPOLO_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class SourceIntegrationTest(unittest.TestCase):

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

    def test_ct_source_schema(self):
        fti = queryUtility(IDexterityFTI, name='Source')
        schema = fti.lookupSchema()
        self.assertEqual(ISource, schema)

    def test_ct_source_fti(self):
        fti = queryUtility(IDexterityFTI, name='Source')
        self.assertTrue(fti)

    def test_ct_source_factory(self):
        fti = queryUtility(IDexterityFTI, name='Source')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ISource.providedBy(obj),
            u'ISource not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_source_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Source',
            id='source',
        )

        self.assertTrue(
            ISource.providedBy(obj),
            u'ISource not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('source', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('source', parent.objectIds())

    def test_ct_source_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Source')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
