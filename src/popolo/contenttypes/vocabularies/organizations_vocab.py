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
                SimpleTerm(value=_(u'orgCatAccountingFirm'),
                           title=_(u'Accounting Firm')),
                SimpleTerm(value=_(u'orgCatParliament'),
                           title=_(u'Parliament')),
                SimpleTerm(value=_(u'orgCatSenate'), title=_(u'Senate')),
                SimpleTerm(value=_(u'orgCatCabinet'), title=_(u'Cabinet')),
                SimpleTerm(value=_(u'orgCatStateExecCouncil'),
                           title=_(u'State Executive Council')),
                SimpleTerm(value=_(u'orgCatStateAssembly'),
                           title=_(u'State Assembly or Legislature')),
                SimpleTerm(value=_(u'orgCatStateGov'),
                           title=_(u'State Government')),
                SimpleTerm(value=_(u'orgCatAgency'),
                           title=_(u'Government Agency')),
                SimpleTerm(value=_(u'orgCatCommission'),
                           title=_(u'Government Commission')),
                SimpleTerm(value=_(u'orgCatDepartment'),
                           title=_(u'Government Department')),
                SimpleTerm(value=_(u'orgCatStateCorp'),
                           title=_(u'State Corporation')),
                SimpleTerm(value=_(u'orgCatPrivateLimitedCo'),
                           title=_(u'Private Limited Company')),
                SimpleTerm(value=_(u'orgCatPublicCo'), title=_(u'Public Company')),
                SimpleTerm(value=_(u'orgCatCommittee'), title=_(u'Committee')),
                SimpleTerm(value=_(u'orgCatBoDirectors'),
                           title=_(u'Board of Directors')),
                SimpleTerm(value=_(u'orgCatManagement'), title=_(u'Management')),
                SimpleTerm(value=_(u'orgCatPP'), title=_(u'Political Party')),
                SimpleTerm(value=_(u'orgCatPPExecutive'),
                           title=_(u'Political Party Executive')),
                SimpleTerm(value=_(u'orgCatPPBranch'),
                           title=_(u'Political Party Branch')),
                SimpleTerm(value=_(u'orgCatTradeAssociation'),
                           title=_(u'Trade Association')),
                SimpleTerm(value=_(u'orgCatLawFirm'),
                           title=_(u'Law Firm')),
                SimpleTerm(value=_(u'orgCatLabourUnion'),
                           title=_(u'Labour Union')),
                SimpleTerm(value=_(u'orgCatCivilSociety'),
                           title=_(u'Civil society')),
            ]
        )

        return organization_categories


OrganizationCategoriesVocabFactory = OrganizationCategoriesVocab()
