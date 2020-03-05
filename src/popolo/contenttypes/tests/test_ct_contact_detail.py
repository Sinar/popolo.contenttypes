# -*- coding: utf-8 -*-
from popolo.contenttypes.content.contact_detail import IContactDetail  # NOQA E501
from popolo.contenttypes.testing import POPOLO_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class ContactDetailIntegrationTest(unittest.TestCase):

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

    def test_ct_contact_detail_schema(self):
        fti = queryUtility(IDexterityFTI, name='Contact Detail')
        schema = fti.lookupSchema()
        self.assertEqual(IContactDetail, schema)

    def test_ct_contact_detail_fti(self):
        fti = queryUtility(IDexterityFTI, name='Contact Detail')
        self.assertTrue(fti)

    def test_ct_contact_detail_factory(self):
        fti = queryUtility(IDexterityFTI, name='Contact Detail')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IContactDetail.providedBy(obj),
            u'IContactDetail not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_contact_detail_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Contact Detail',
            id='contact_detail',
        )

        self.assertTrue(
            IContactDetail.providedBy(obj),
            u'IContactDetail not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('contact_detail', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('contact_detail', parent.objectIds())

    def test_ct_contact_detail_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Contact Detail')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
