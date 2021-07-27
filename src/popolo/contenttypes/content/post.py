# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from collective import dexteritytextindexer
from z3c.relationfield.schema import RelationChoice
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives

from popolo.contenttypes import _


class IPost(model.Schema):
    """ Marker interface and Dexterity Python Schema for Post
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('post.xml')

    dexteritytextindexer.searchable('label')
    label = schema.TextLine(
        title=_(u'Label'),
        description=_(u"A describing the Post"),
        required=True,
        )

    dexteritytextindexer.searchable('role')
    role = schema.TextLine(
        title=_(u'Role'),
        description=_(u"The function that the holder of the " +
                      "post fulfills"),
        required=True,)

    # Organization
    directives.widget('organization',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )
    organization = RelationChoice(
            title=u'Organization',
            source=CatalogSource(portal_type='Organization'),
            required=False,
            )

    start_date = schema.Date(
        title=_(u'Start Date'),
        description=_(u'Date this post was created'),
        required=False,)

    end_date = schema.Date(
        title=_('End Date'),
        description=_(u'Date which this post was eliminated'),
        required=False,)

    # Memberships implemented as view
    # Links implemmented as content items
    # Area implemented as content item
    # Contact Details as content item


@implementer(IPost)
class Post(Container):
    """
    """

    @property
    def title(self):
        ''' return label'''
        return self.label

    @title.setter
    def title(self, value):
        ''' we wont set a title here'''
        pass

    @property
    def description(self):
        ''' return role'''
        return self.role

    @description.setter
    def description(self, value):
        ''' we wont set a title here'''
        pass
