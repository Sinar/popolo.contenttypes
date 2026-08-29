# -*- coding: utf-8 -*-
from politikus.popolo.testing import POLITIKUS_POPOLO_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import IVocabularyTokenized

import unittest


class GeonameFeaturecodesVocabIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_POPOLO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_vocab_geoname_featurecodes_vocab(self):
        vocab_name = 'politikus.popolo.geonamefeaturecodes'
        factory = getUtility(IVocabularyFactory, vocab_name)
        self.assertTrue(IVocabularyFactory.providedBy(factory))

        vocabulary = factory(self.portal)
        self.assertTrue(IVocabularyTokenized.providedBy(vocabulary))
        terms = list(vocabulary)
        self.assertGreater(len(terms), 600)
        values = [t.value for t in terms]
        for expected in ('A.ADM1', 'A.PCL', 'P.PPLA2'):
            self.assertIn(expected, values)
        self.assertEqual(
            vocabulary.getTerm('A.ADM1').title,
            u'first-order administrative division',
        )
