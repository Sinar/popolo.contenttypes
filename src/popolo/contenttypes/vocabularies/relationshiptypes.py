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
class relationshiptypes(object):
    """
    """

    def __call__(self, context):

        relationship_types = SimpleVocabulary(
            [
                SimpleTerm(value=_(u'spouse'),
                           title=_(u'Spouse')),
                SimpleTerm(value=_(u'parent'),
                           title=_(u'Parent')),
                SimpleTerm(value=_(u'business_partner'),
                           title=_(u'Business Partner')),
                SimpleTerm(value=_(u'associate'),
                           title=_(u'Associate')),
                SimpleTerm(value=_(u'romantic'),
                           title=_(u'Romantic Partner')),
                SimpleTerm(value=_(u'employer'),
                           title=_(u'Employer')),
                SimpleTerm(value=_(u'subordinate'),
                           title=_(u'Subordinate')),
            ]
            )

        return relationship_types


RelationshiptypesFactory = relationshiptypes()
