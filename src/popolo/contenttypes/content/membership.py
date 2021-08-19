# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from collective import dexteritytextindexer
from z3c.relationfield.schema import RelationChoice

from plone.app.vocabularies.catalog import CatalogSource

from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives

from zope.interface import implementer

from popolo.contenttypes import _


class IMembership(model.Schema):
    """ Marker interface and Dexterity Python Schema for Membership
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('membership.xml')

    dexteritytextindexer.searchable('label')
    label = schema.TextLine(
        title=_(u'Label'),
        description=_(u"A label describing the membership, " +
                      "eg. Member of Parliament of Kericho County"),
        required=True,)

    dexteritytextindexer.searchable('role')
    role = schema.TextLine(
        title=_(u'Role'),
        description=_(u"A role that the member fulfills in, " +
                      "in the organization. eg. " +
                      "Member of Parliament"),
        required=True,)

    # Person
    directives.widget('person',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    person = RelationChoice(
            title=u'Person',
            source=CatalogSource(portal_type='Person'),
            required=True,
            )

    # Organization
    directives.widget('organization',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )
    organization = RelationChoice(
            title=u'Organization',
            source=CatalogSource(portal_type='Organization'),
            required=True,
            )

    # Post
    directives.widget('post',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    post = RelationChoice(
            title=u'Post',
            source=CatalogSource(portal_type='Post'),
            required=False,
            )

    # On Behalf Of
    directives.widget('on_behalf_of',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )
    on_behalf_of = RelationChoice(
            title=_(u'On Behalf Of'),
            description=_(u'The organization on whose behalf the ' +
                          'person is a member of the organization'),
            source=CatalogSource(portal_type='Organization'),
            required=False,
            )

    start_date = schema.Date(
        title=_(u'Start Date'),
        description=_(u'Date which this relationship began'),
        required=False,)

    end_date = schema.Date(
        title=_('End Date'),
        description=_(u'Date which this relationship ended'),
        required=False,)

@implementer(IMembership)
class Membership(Container):
    """
    """

    @property
    def title(self):
        ''' return label'''
        return self.label

    @title.setter
    def title(self, value):
        ''' we wont set a title here'''
        pass

    @property
    def description(self):
        ''' return role'''
        return self.role

    @description.setter
    def description(self, value):
        ''' we wont set a title here'''
        pass
