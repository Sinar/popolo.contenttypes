# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Item
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import implementer

from collective import dexteritytextindexer

from popolo.contenttypes import _

contact_types = SimpleVocabulary(
        [
            SimpleTerm(value=u'cell', title=_(u'Mobile Phone Number')),
            SimpleTerm(value=u'voice', title=_(u'Voice Phone Number')),
            SimpleTerm(value=u'text',
                       title=_(u'A Phone number for text messages')),
            SimpleTerm(value=u'email', title=_(u'An email address')),
            SimpleTerm(value=u'address', title=_(u'A postal address')),
            SimpleTerm(value=u'url', title=_(u'A URL to a contact form')),
            SimpleTerm(value=u'twitter', title=_(u'Twitter Handle')),
        ],
)


class IContactDetail(model.Schema):
    """ Marker interface and Dexterity Python Schema for ContactDetail
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('contact_detail.xml')

    dexteritytextindexer.searchable('label')
    label = schema.TextLine(
        title=_(u'Label'),
        description=_(u"A human-readable label for the contact detail"),
        )

    type = schema.Choice(
        title=_(u'Type'),
        description=_(u'A type of medium, eg. mobile phone or email'),
        vocabulary=contact_types,
        )

    dexteritytextindexer.searchable('value')
    value = schema.TextLine(
        title=_(u'Value'),
        description=_(u"A value, e.g. a phone number or email address"),
        )

    dexteritytextindexer.searchable('note')
    note = schema.Text(
        title=_(u'Note'),
        description=_(u"A note, e.g. for grouping contact details by " +
                      u"physical location"),
        required=False,
        )

    # valid_from and valid_until will use Plone's effective_date
    # and expiry_date standard fields


@implementer(IContactDetail)
class ContactDetail(Item):
    """
    """

    def Title(self):
        return self.label

    @property
    def title(self):
        return self.label
