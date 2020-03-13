# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
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
    """

    # TODO check with K. to see if any property could have more efficient field
    title = schema.TextLine(
        title=_(u'Organization Name'),
        required=True,)

    alternate_names = schema.List(
        title=_(u'Alternate Names'),
        description=_(u'Any other names or name contractions ' +
                      'the organization is currently known under'),
        required=False,
        value_type=schema.TextLine(
            title=_(u'Alternate Name'),),)

    former_names = schema.List(
        title=_(u'Former Names'),
        description=_(u'All other names or name contractions ' +
                      'the organization used to be known under'),
        required=False,
        value_type=schema.TextLine(
            title=_(u'Former Name & Years of Usage'),),)

    # TODO look at standard reuse for use of correct fields in some properties
    identifiers = schema.Object(
        title=u'Identifiers',
        required=False,
        schema=identifier.IIdentifier,)

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

    # TODO find geographic area as popolo contenttype?? Or use a voc???
    """geographic_area = schema.Object(
    title=u'Geographic Area',
    required=False,
    schema=area.IArea,)"""

    one_line_description = schema.TextLine(
        title=_(u'One-line Description'),
        description=_(u'One line to tell what is the organization about'),
        required=False,)

    summary = schema.Text(
        title=_(u'Description'),
        required=False,)

    date_of_founding = schema.Date(
        title=_('Date of Founding'),
        required=False,)

    date_of_dissolution = schema.Date(
        title=_('Date of Dissolution'),
        required=False,)

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
        return self.summary

    @description.setter
    def description(self, value):
        ''' we wont set a description here'''
        pass
