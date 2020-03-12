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


class IOtherName(model.Schema):
    """ Marker interface and Dexterity Python Schema for OtherName
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('other_name.xml')

    dexteritytextindexer.searchable('name')
    name = schema.TextLine(
                title=_(u'Name'),
                required=False,
                )

    dexteritytextindexer.searchable('note')
    note = schema.Text(
                title=_(u'Note'),
                description=_(u'Birth name'),
                required=False,
                )

    start_date = schema.Date(
                title=_(u'Start Date'),
                required=False,
                )

    end_date = schema.Date(
                title=_(u'End Date'),
                required=False,
                )


@implementer(IOtherName)
class OtherName(Item):
    """
    """

    @property
    def title(self):
        return self.name

    @title.setter
    def title(self, value):
        ''' we wont set a title here'''
        pass
