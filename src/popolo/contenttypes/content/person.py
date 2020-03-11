# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedimage
from plone.namedfile import field
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer

from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from collective import dexteritytextindexer

from popolo.contenttypes import _


class IPerson(model.Schema):
    """ Marker interface and Dexterity Python Schema for Person
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('person.xml')

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u'A person\'s preferred full name'),
        )

    dexteritytextindexer.searchable('description')
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'One line description of this person'),
        )

    gender = schema.Choice(
        title=_(u'Gender'),
        vocabulary=SimpleVocabulary([
            SimpleTerm(value=u'male', title=_(u'Male')),
            SimpleTerm(value=u'female', title=_(u'Female')),
            SimpleTerm(value=u'other', title=_(u'Other'))]
            ),
        required=False,
        )

    birth_date = schema.Date(
        title=_(u'Date of Birth'),
        required=False,
        )

    death_date = schema.Date(
        title=_(u'Date of Death'),
        required=False,
        )

    image = field.NamedImage(
        title=_(u"Headshot"),
        description=_(u'Image file of a headshot person'),
        required=False,
        )

    dexteritytextindexer.searchable('biography')
    notes = RichText(
         title=_(u'Biography'),
         description=_(u'Detailed biography of this person'),
         required=False,
     )

    dexteritytextindexer.searchable('notes')
    notes = RichText(
         title=_(u'Notes'),
         required=False
     )


@implementer(IPerson)
class Person(Container):
    """
    """
