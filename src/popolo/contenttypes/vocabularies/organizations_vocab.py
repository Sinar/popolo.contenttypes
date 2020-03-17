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
                SimpleTerm(value=_(u'orgCatParliament'), title=_(u'Parliament')),
                SimpleTerm(value=_(u'orgCatSenate'), title=_(u'Senate')),
                SimpleTerm(value=_(u'orgCatCabinet'), title=_(u'Cabinet')),
                SimpleTerm(value=_(u'orgCatStateExecCouncil'),
                           title=_(u'State executive council')),
                SimpleTerm(value=_(u'orgCatStateAssembly'),
                           title=_(u'State assembly')),
                SimpleTerm(value=_(u'orgCatStateGov'), title=_(u'State government')),
                SimpleTerm(value=_(u'orgCatDepartment'), title=_(u'Department')),
                SimpleTerm(value=_(u'orgCatStateCorp'),
                           title=_(u'State Corporation')),
                SimpleTerm(value=_(u'orgCatPrivateLimitedCo'),
                           title=_(u'Private limited company')),
                SimpleTerm(value=_(u'orgCatPublicCo'), title=_(u'Public company')),
                SimpleTerm(value=_(u'orgCatCommittee'), title=_(u'Committee')),
                SimpleTerm(value=_(u'orgCatBoDirectors'),
                           title=_(u'Board of directors')),
                SimpleTerm(value=_(u'orgCatManagement'), title=_(u'Management')),
                SimpleTerm(value=_(u'orgCatPP'), title=_(u'Political party')),
                SimpleTerm(value=_(u'orgCatPPExecutive'),
                           title=_(u'Political party executive')),
                SimpleTerm(value=_(u'orgCatPPBranch'),
                           title=_(u'Political party branch')),
                SimpleTerm(value=_(u'orgCatTradeAssociation'),
                           title=_(u'Trade association')),
                SimpleTerm(value=_(u'orgCatLabourUnion'),
                           title=_(u'Labour union')),
                SimpleTerm(value=_(u'orgCatCivilSociety'),
                           title=_(u'Civil society')),
            ]
        )

        return organization_categories


OrganizationCategoriesVocabFactory = OrganizationCategoriesVocab()
