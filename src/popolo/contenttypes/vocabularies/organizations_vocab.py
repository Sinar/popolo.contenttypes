# -*- coding: utf-8 -*-

# from plone import api
from popolo.contenttypes import _
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class OrganizationCategoriesVocab(object):
    """
    """

    def __call__(self, context):

        organization_categories = SimpleVocabulary(
            [
                SimpleTerm(value=(u'orgCatAccountingFirm'),
                           title=_(u'Accounting Firm')),
                SimpleTerm(value=(u'orgCatParliament'),
                           title=_(u'Parliament')),
                SimpleTerm(value=(u'orgCatSenate'), title=_(u'Senate')),
                SimpleTerm(value=(u'orgCatCabinet'), title=_(u'Cabinet')),
                SimpleTerm(value=(u'orgCatStateExecCouncil'),
                           title=_(u'State Executive Council')),
                SimpleTerm(value=(u'orgCatStateAssembly'),
                           title=_(u'State Assembly or Legislature')),
                SimpleTerm(value=(u'orgCatStateGov'),
                           title=_(u'State Government')),
                SimpleTerm(value=(u'orgCatAgency'),
                           title=_(u'Government Agency')),
                SimpleTerm(value=(u'orgCatCommission'),
                           title=_(u'Government Commission')),
                SimpleTerm(value=(u'orgCatDepartment'),
                           title=_(u'Government Department')),
                SimpleTerm(value=(u'orgCatStateCorp'),
                           title=_(u'State Corporation')),
                SimpleTerm(value=(u'orgCatPrivateLimitedCo'),
                           title=_(u'Private Limited Company')),
                SimpleTerm(value=(u'orgCatPublicCo'), title=_(u'Public Company')),
                SimpleTerm(value=(u'orgCatCommittee'), title=_(u'Committee')),
                SimpleTerm(value=(u'orgCatBoDirectors'),
                           title=_(u'Board of Directors')),
                SimpleTerm(value=(u'orgCatManagement'), title=_(u'Management')),
                SimpleTerm(value=(u'orgCatPP'), title=_(u'Political Party')),
                SimpleTerm(value=(u'orgCatPPExecutive'),
                           title=_(u'Political Party Executive')),
                SimpleTerm(value=(u'orgCatPPBranch'),
                           title=_(u'Political Party Branch')),
                SimpleTerm(value=(u'orgCatTradeAssociation'),
                           title=_(u'Trade Association')),
                SimpleTerm(value=(u'orgCatLawFirm'),
                           title=_(u'Law Firm')),
                SimpleTerm(value=(u'orgCatLabourUnion'),
                           title=_(u'Labour Union')),
                SimpleTerm(value=(u'orgCatCivilSociety'),
                           title=_(u'Civil society')),
                SimpleTerm(value=(u'orgCatFinancialInstitution'),
                           title=_(u'Financial Institution')),
            ]
        )

        return organization_categories


OrganizationCategoriesVocabFactory = OrganizationCategoriesVocab()
