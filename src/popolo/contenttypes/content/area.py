# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from plone.dexterity.content import Item
from z3c.relationfield.schema import RelationChoice
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

from collective import dexteritytextindexer

from plone.app.vocabularies.catalog import CatalogSource

from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives


from popolo.contenttypes import _


class IArea(model.Schema):
    """ Marker interface and Dexterity Python Schema for Area
        Reference Schema Popolo-spec Area JSON Schema
        https://www.popoloproject.com/specs/area.html
    """
    # The Area class should have properties for: name, identifier, classification, parent area, geometry.
    dexteritytextindexer.searchable('name')
    name = schema.TextLine(
        title=_(u'Area Name'),
        description=_(u'A primary name, e.g. a legally recognized ' +
                      'name'),
        required=True,)
    
    classification = schema.Choice(
        title=_(u'Area Classification'),
        description=_(u'An area category, e.g. city'),
        required=False,
        vocabulary='popolo.contenttypes.geonamefeaturecodes',
        )
    
    directives.widget('parent_area',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    parent_area = RelationChoice(
            title=_(u'Parent Area'),
            description=_(u'The area that contains this area'),
            source=CatalogSource(portal_type='Area'),
            required=False,
            )

    dexteritytextindexer.searchable('identifier')
    description = schema.Text(
        title=_(u'Identifier'),
        description=_(u'An issued identifier, e.g. an Open Civic Data Division Identifier'),
        required=False,)

    description = schema.Text(
        title=_(u'Geometry'),
        description=_(u'A geometry'),
        required=False,)


@implementer(IArea)
class Area(Item):
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
