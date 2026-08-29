# -*- coding: utf-8 -*-
from politikus.popolo import utils
from politikus.popolo.testing import POLITIKUS_POPOLO_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import createObject
from zope.component import getUtility
from zope.component import queryUtility
from zope.intid.interfaces import IIntIds
from plone.dexterity.interfaces import IDexterityFTI
from z3c.relationfield import RelationValue

import unittest


def relation_to(obj):
    """A storable RelationValue pointing at the given content object."""
    return RelationValue(getUtility(IIntIds).getId(obj))


class UtilsIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_POPOLO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.person_a = api.content.create(
            self.portal, 'Person', 'person-a', name=u'Person A')
        self.person_b = api.content.create(
            self.portal, 'Person', 'person-b', name=u'Person B')
        self.relationship = api.content.create(
            self.person_a, 'Relationship', 'relationship',
            name=u'Son of',
            relationship_subject=relation_to(self.person_a),
            relationship_object=relation_to(self.person_b),
        )

    def test_get_intid(self):
        """A persisted object has an intid."""
        intid = utils.get_intid(self.person_a)
        self.assertIsNotNone(intid)
        self.assertEqual(
            intid,
            getUtility(IIntIds).getId(self.person_a),
        )

    def test_get_intid_not_in_zodb(self):
        """An object that was never saved has no intid."""
        fti = queryUtility(IDexterityFTI, name='Person')
        obj = createObject(fti.factory)
        self.assertIsNone(utils.get_intid(obj))

    def test_get_relations_without_intid(self):
        """No intid -> no relations, no error."""
        fti = queryUtility(IDexterityFTI, name='Person')
        obj = createObject(fti.factory)
        self.assertEqual(list(utils.get_relations(obj)), [])
        self.assertEqual(
            list(utils.get_relations(obj, attribute='name')), [])
        self.assertEqual(list(utils.get_backrelations(obj)), [])

    def test_get_relations_forward(self):
        """Forward relations can be constrained by attribute."""
        relations = list(utils.get_relations(
            self.relationship,
            attribute='relationship_subject',
        ))
        self.assertEqual(len(relations), 1)
        self.assertEqual(
            relations[0].to_id,
            utils.get_intid(self.person_a),
        )

    def test_get_relations_all_attributes(self):
        """Without an attribute constraint all relation types are returned."""
        relations = list(utils.get_relations(self.relationship))
        to_ids = sorted(rel.to_id for rel in relations)
        self.assertEqual(
            to_ids,
            sorted([
                utils.get_intid(self.person_a),
                utils.get_intid(self.person_b),
            ]),
        )

    def test_get_backrelations(self):
        """Backreferences are found on the referenced object."""
        relations = list(utils.get_backrelations(
            self.person_a,
            attribute='relationship_subject',
        ))
        self.assertEqual(len(relations), 1)
        self.assertEqual(
            relations[0].from_id,
            utils.get_intid(self.relationship),
        )

    def test_get_backrelations_unrelated(self):
        """An object without inbound relations has no backreferences."""
        self.assertEqual(
            list(utils.get_backrelations(
                self.person_b,
                attribute='relationship_subject',
            )),
            [],
        )
