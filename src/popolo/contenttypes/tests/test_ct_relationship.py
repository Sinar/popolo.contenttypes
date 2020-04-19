# -*- coding: utf-8 -*-
from popolo.contenttypes.content.relationship import IRelationship  # NOQA E501
from popolo.contenttypes.testing import POPOLO_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class RelationshipIntegrationTest(unittest.TestCase):

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

    def test_ct_relationship_schema(self):
        fti = queryUtility(IDexterityFTI, name='Relationship')
        schema = fti.lookupSchema()
        self.assertEqual(IRelationship, schema)

    def test_ct_relationship_fti(self):
        fti = queryUtility(IDexterityFTI, name='Relationship')
        self.assertTrue(fti)

    def test_ct_relationship_factory(self):
        fti = queryUtility(IDexterityFTI, name='Relationship')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IRelationship.providedBy(obj),
            u'IRelationship not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_relationship_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Relationship',
            id='relationship',
        )

        self.assertTrue(
            IRelationship.providedBy(obj),
            u'IRelationship not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('relationship', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('relationship', parent.objectIds())

    def test_ct_relationship_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Relationship')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_relationship_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Relationship')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'relationship_id',
            title='Relationship container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
