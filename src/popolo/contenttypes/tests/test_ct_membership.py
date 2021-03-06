# -*- coding: utf-8 -*-
from popolo.contenttypes.content.membership import IMembership  # NOQA E501
from popolo.contenttypes.testing import POPOLO_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class MembershipIntegrationTest(unittest.TestCase):

    layer = POPOLO_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_membership_schema(self):
        fti = queryUtility(IDexterityFTI, name='Membership')
        schema = fti.lookupSchema()
        self.assertEqual(IMembership, schema)

    def test_ct_membership_fti(self):
        fti = queryUtility(IDexterityFTI, name='Membership')
        self.assertTrue(fti)

    def test_ct_membership_factory(self):
        fti = queryUtility(IDexterityFTI, name='Membership')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IMembership.providedBy(obj),
            u'IMembership not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_membership_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Membership',
            id='membership',
        )

        self.assertTrue(
            IMembership.providedBy(obj),
            u'IMembership not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('membership', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('membership', parent.objectIds())

    def test_ct_membership_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Membership')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_membership_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Membership')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'membership_id',
            title='Membership container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
