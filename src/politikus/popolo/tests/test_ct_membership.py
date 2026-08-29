# -*- coding: utf-8 -*-
from politikus.popolo.content.membership import IMembership  # NOQA E501
from politikus.popolo.testing import POLITIKUS_POPOLO_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class MembershipIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_POPOLO_INTEGRATION_TESTING

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
        # Membership is not globally addable, so construct it directly.
        portal_types = self.portal.portal_types
        obj_id = portal_types.constructContent(
            'Membership',
            self.portal,
            'membership',
        )
        obj = self.portal[obj_id]

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

    def test_ct_membership_not_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Membership')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable, it should only be added '
            u'under its parent types!'.format(fti.id)
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

    def test_ct_membership_title_description_aliases(self):
        """title mirrors label and description mirrors role."""
        fti = queryUtility(IDexterityFTI, name='Membership')
        obj = createObject(fti.factory)
        obj.label = u'Member of Parliament'
        obj.role = u'MP'
        self.assertEqual(obj.title, u'Member of Parliament')
        self.assertEqual(obj.description, u'MP')
        obj.title = u'Ignored'
        obj.description = u'Also ignored'
        self.assertEqual(obj.title, u'Member of Parliament')
        self.assertEqual(obj.description, u'MP')
