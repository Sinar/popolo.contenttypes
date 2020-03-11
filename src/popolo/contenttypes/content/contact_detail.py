# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Item
# from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.dexterity.content import Container
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from popolo.contenttypes import _

contact_types = SimpleVocabulary([
            SimpleTerm(value=u'cell', title=_(u'Mobile Phone Number')),
            SimpleTerm(value=u'voice', title=_(u'Voice Phone Number')),
            SimpleTerm(value=u'email', title=_(u'Email Address')),
            SimpleTerm(value=u'address', title=_(u'Full street address')),
            SimpleTerm(value=u'twitter', title=_(u'Twitter Handle')),
            SimpleTerm(value=u'facebook', 
                title=_(u'Facebook URL')),
            ]
            )

class IContactDetail(model.Schema):
    """ Marker interface and Dexterity Python Schema for ContactDetail
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('contact_detail.xml')

    title = schema.TextLine(
        title=_(u'Label'),
        description=_(u"A human-readable label for the contact detail"),
        )

    type = schema.Choice(
        title=_(u'Type of Medium'),
        vocabulary=contact_types,
        required=True,
        )

    value = schema.TextLine(
            title=_(u'Value'),
            description=_(u'eg. +60 323 4344 for mobile,' +
                          ' myemailaddress.com for email')
            )

    note = schema.Text(
            title=_(u'Note'),
            description=_(u'A note, e.g. for grouping contact details by ' +
                          'physical location',),
                    )

    # TODO Add start_date and end_date for valid_from and valid_until
    # fields

    # directivesmil.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )

@implementer(IContactDetail)
class ContactDetail(Container):
    """
    """
