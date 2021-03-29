# -*- coding: utf-8 -*-

from popolo.contenttypes import _
from plone.autoform import directives
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from plone.supermodel.directives import primary
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class IImageRightsMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IImageRights(model.Schema):
    """
    """

    directives.order_after(image_rights = 'image')
    image_rights = schema.TextLine(
        title=_(u'Image Rights'),
        description=_(u'Copyright statement or other rights information on this item.'),
        required=False,
    )


@implementer(IImageRights)
@adapter(IImageRightsMarker)
class ImageRights(object):
    def __init__(self, context):
        self.context = context

    @property
    def image_rights(self):
        if safe_hasattr(self.context, 'image_rights'):
            return self.context.image_rights
        return None

    @image_rights.setter
    def image_rights(self, value):
        self.context.image_rights = value
