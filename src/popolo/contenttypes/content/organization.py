# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from plone.namedfile import field
from zope import schema
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import implementer

from popolo.contenttypes import _
from popolo.contenttypes.content import contact_detail
from popolo.contenttypes.content import identifier

# TODO importing itself?? How to reference IOrganization?
# from plone.formwidget.contenttree import ObjPathSourceBinder
# from z3c.relationfield.schema import RelationChoice
# from popolo.contenttypes.content import organization

# TODO ask K. if there is an area popolo content type.
# from popolo.contenttypes.content import area

# TODO : determine if better place to put this.
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
        SimpleTerm(value=_(u'orgCatCivilSociety'), title=_(u'Civil society'))
    ]
)


class IOrganization(model.Schema):
    """ Marker interface and Dexterity Python Schema for Organization
        Reference Schema Popolo-spec Organization JSON Schema
        https://www.popoloproject.com/specs/organization.html
    """

    name = schema.TextLine(
        title=_(u'Organization Name'),
        description=_(u"A primary name, e.g. a legally recognized " +
                      "name"),
        required=True,)

    # other_names implemented as content type

    # identifiers applied as content type

    classification = schema.Choice(
        title=_('Organization Classification'),
        required=False,
        vocabulary=organization_categories,)

    # TODO make this work with relations to IOrganization
    """parent_organization = RelationChoice(
        title=_(u'Parent Organization'),
        required=False,
        source=ObjPathSourceBinder(
            object_provides=organization.IOrganization.__identifier__),)"""

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
    founding_date = schema.Date(
        title=_('Date of Founding'),
        required=False,)

    dissolution_date = schema.Date(
        title=_('Date of Dissolution'),
        required=False,)

    description = schema.Text(
        title=_(u'Description'),
        required=True,)

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

    @property
    def description(self):
        ''' return description'''
        return self.description

    @description.setter
    def description(self, value):
        ''' we wont set a description here'''
        pass
