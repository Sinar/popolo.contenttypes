# -*- coding: utf-8 -*-
from popolo.contenttypes.content.area import IArea  # NOQA E501
from popolo.contenttypes.testing import POPOLO_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class AreaIntegrationTest(unittest.TestCase):

    layer = POPOLO_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_area_schema(self):
        fti = queryUtility(IDexterityFTI, name='Area')
        schema = fti.lookupSchema()
        self.assertEqual(IArea, schema)

    def test_ct_area_fti(self):
        fti = queryUtility(IDexterityFTI, name='Area')
        self.assertTrue(fti)

    def test_ct_area_factory(self):
        fti = queryUtility(IDexterityFTI, name='Area')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IArea.providedBy(obj),
            u'IArea not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_area_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Area',
            id='area',
        )

        self.assertTrue(
            IArea.providedBy(obj),
            u'IArea not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('area', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('area', parent.objectIds())

    def test_ct_area_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Area')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
