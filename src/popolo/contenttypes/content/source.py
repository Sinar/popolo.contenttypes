# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item

# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from plone.app.z3cform.widget import LinkFieldWidget

from zope import schema
from zope.interface import implementer


from popolo.contenttypes import _

class ISource(model.Schema):
    """ Marker interface and Dexterity Python Schema for Source
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('source.xml')

# TODO A Selection field of fields in Parent Object

    directives.widget('url', LinkFieldWidget)
    url = schema.TextLine(title=_(u'Source Link'),)


@implementer(ISource)
class Source(Item):
    """
    """
