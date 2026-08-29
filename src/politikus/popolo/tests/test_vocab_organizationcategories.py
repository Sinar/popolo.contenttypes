# -*- coding: utf-8 -*-
from politikus.popolo.testing import POLITIKUS_POPOLO_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import IVocabularyTokenized

import unittest


class OrganizationcategoriesVocabIntegrationTest(unittest.TestCase):
    # The package registers 'politikus.popolo.organizationcategories'
    # (the OrganizationCategoriesVocab factory); there is no
    # 'OrganizationsVocab' registration.

    layer = POLITIKUS_POPOLO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_vocab_organizationcategories(self):
        vocab_name = 'politikus.popolo.organizationcategories'
        factory = getUtility(IVocabularyFactory, vocab_name)
        self.assertTrue(IVocabularyFactory.providedBy(factory))

        vocabulary = factory(self.portal)
        self.assertTrue(IVocabularyTokenized.providedBy(vocabulary))
        terms = list(vocabulary)
        self.assertEqual(len(terms), 24)
        values = [t.value for t in terms]
        for expected in (
            'orgCatParliament',
            'orgCatSenate',
            'orgCatAgency',
            'orgCatPP',
            'orgCatTradeAssociation',
            'orgCatFinancialInstitution',
        ):
            self.assertIn(expected, values)
        self.assertEqual(
            vocabulary.getTerm('orgCatParliament').title,
            u'Parliament',
        )
