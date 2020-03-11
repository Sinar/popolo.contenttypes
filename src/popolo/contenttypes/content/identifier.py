# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Item
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from collective import dexteritytextindexer


from popolo.contenttypes import _


class IIdentifier(model.Schema):
    """ Marker interface and Dexterity Python Schema for Identifier
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('identifier.xml')

    scheme = schema.TextLine(
                title=_(u'Scheme'),
                description=_(u'Type eg. IC Number, Passport, ' +
                              u'Company Registration Number'),
                required=False,
                )

    dexteritytextindexer.searchable('identifier')
    identifier = schema.TextLine(
                title=_(u'Identifier'),
                description=_(u'Unique value as code or number'),
                required=False,
                )


@implementer(IIdentifier)
class Identifier(Item):
    """
    """

    def Title(self):
        return self.scheme

    @property
    def title(self):
        return self.scheme
