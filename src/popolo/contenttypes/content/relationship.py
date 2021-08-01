# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from plone.app.z3cform.widget import SelectFieldWidget
from zope import schema
from collective import dexteritytextindexer
from z3c.relationfield.schema import RelationChoice

from plone.app.vocabularies.catalog import CatalogSource

from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives

from zope.interface import implementer

from popolo.contenttypes import _


class IRelationship(model.Schema):
    """ Marker interface and Dexterity Python Schema for Relationship
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('relationship.xml')

    dexteritytextindexer.searchable('name')
    name = schema.TextLine(
        title=_(u'Relationship Name'),
        description=_(u'''The name of this relationship, eg. Son of Person,
        Known business associate of Person, Major client of Business.'''),
        required=True,
        )

    dexteritytextindexer.searchable('description')
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'Brief description of this relationship'),
        required=False,
        )

    # Relationship Type

    directives.widget(relationship_type=SelectFieldWidget)
    relationship_type = schema.Choice(
        title=_('Relationship type'),
        required=False,
        vocabulary='popolo.contenttypes.relationshiptypes',
        )

    # Subject
    directives.widget('relationship_subject',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )
    relationship_subject = RelationChoice(
            title=u'Subject',
            description=_(u'The subject of the relation.'),
            source=CatalogSource(portal_type=['Person', 'Organization']),
            required=False,
            )

    # Object
    directives.widget('relationship_object',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    relationship_object = RelationChoice(
            title=u'Object',
            description=_(u'The object of the relation.'),
            source=CatalogSource(portal_type=['Person', 'Organization']),
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

    # Public notes
    dexteritytextindexer.searchable('notes')
    notes = RichText(
         title=_(u'Notes'),
         required=False
     )


@implementer(IRelationship)
class Relationship(Container):
    """
    """

    @property
    def title(self):
        ''' return name'''
        return self.name

    @title.setter
    def title(self, value):
        ''' we wont set a title here'''
        pass
