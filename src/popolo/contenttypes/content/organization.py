# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.app.textfield import RichText
from plone.supermodel import model
from plone.namedfile import field
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import implementer
from collective import dexteritytextindexer

from plone.app.vocabularies.catalog import CatalogSource

from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives

from popolo.contenttypes import _


class IOrganization(model.Schema):
    """ Marker interface and Dexterity Python Schema for Organization
        Reference Schema Popolo-spec Organization JSON Schema
        https://www.popoloproject.com/specs/organization.html
    """

    dexteritytextindexer.searchable('name')
    name = schema.TextLine(
        title=_(u'Organization Name'),
        description=_(u"A primary name, e.g. a legally recognized " +
                      "name"),
        required=True,)

    # other_names implemented as content type

    # identifiers applied as content type

    # TODO area field use popolo Area class (content type)
    # https://github.com/Sinar/popolo.contenttypes/issues/12

    # We will not use abstract (one liner) field from popolo-spec for
    # now
    '''
    abstract = schema.Text(
        title=_(u'One-line Description'),
        description=_(u'One line to tell what is the organization about'),
        required=False,)
    '''

    directives.widget('parent_organization',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    parent_organization = RelationChoice(
            title=u'Parent Org',
            source=CatalogSource(portal_type='Organization'),
            required=False,
            )

    dexteritytextindexer.searchable('description')
    description = schema.Text(
        title=_(u'Description'),
        required=False,)

    classification = schema.Choice(
        title=_('Organization Classification'),
        required=False,
        vocabulary='popolo.contenttypes.organizationcategories',
        )

    founding_date = schema.Date(
        title=_('Date of Founding'),
        required=False,)

    dissolution_date = schema.Date(
        title=_('Date of Dissolution'),
        required=False,)

    image = field.NamedImage(
        title=_(u"Logo"),
        description=_(u'Official logo or emblem of organization'),
        required=False,
        )

    # contact_details implemented as content type in container

    # links implemented as content type in container

    # TODO memberships to be implemented as content type

    # TODO posts to be implemeted as content type

    # motions not implemented for now
    # votes not implemented for now

    # children to be implemented as view of back references to parent_id

    # created, updated using Plone/Dublin Core effective 
    # and expiry date fields

    # sources to use content type

    dexteritytextindexer.searchable('notes')
    notes = RichText(
         title=_(u'Notes'),
         required=False
     )


@implementer(IOrganization)
class Organization(Container):
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
