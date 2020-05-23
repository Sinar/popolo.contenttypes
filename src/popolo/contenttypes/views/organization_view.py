# -*- coding: utf-8 -*-

from plone import api
from popolo.contenttypes import _
from Products.Five.browser import BrowserView
from plone.dexterity.browser.view import DefaultView
import popolo.contenttypes.utils as utils

from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


class OrganizationView(DefaultView,BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('organization_view.pt')

    # TODO These are old functions, and could be rewritten better.

    def child_orgs(self):
        """
        Return back references from source object on specified attribute_name
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        attribute_name = 'parent_organization'

        result = []

        for rel in catalog.findRelations(
            dict(to_id=intids.getId(aq_inner(source_object)),
                                    from_attribute=attribute_name)
              ):
           
            obj = intids.queryObject(rel.from_id)

            if obj is not None and checkPermission('zope2.View', obj):
                result.append(obj)

        return result

    def members(self):
        """
        Return back references from source object on specified attribute_name
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        attribute_name = 'organization'

        result = []

        for rel in catalog.findRelations(
            dict(to_id=intids.getId(aq_inner(source_object)),
                                    from_attribute=attribute_name)
              ):
           
            obj = intids.queryObject(rel.from_id)

            if obj is not None and checkPermission('zope2.View', obj):
                if obj.portal_type == 'Membership' and obj.post is None:
                    # check if person has membership
                    if obj.person:
                        result.append(obj)

        return result


    def posts(self):
        """
        Return back references from source object on specified attribute_name
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        attribute_name = 'organization'

        result = []

        for rel in catalog.findRelations(
            dict(to_id=intids.getId(aq_inner(source_object)),
                                    from_attribute=attribute_name)
              ):
           
            obj = intids.queryObject(rel.from_id)

            if obj is not None and checkPermission('zope2.View', obj):
                if obj.portal_type == 'Post':

                    obj.members = []

                    for membership in catalog.findRelations(
                        dict(to_id=intids.getId(aq_inner(obj)),)
                          ):
                        member = intids.queryObject(membership.from_id)
                        # check for person
                        if member.person:
                            obj.members.append(member)

                    result.append(obj)

        return result

    def relationships_subject(self):
        # Get relationships where person or organization is the subject

        """
        Return back references from source object on specified attribute_name
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context

        result = []

        for rel in catalog.findRelations(
            dict(to_id=intids.getId(aq_inner(source_object)),
                 from_attribute='relationship_subject')
              ):

            obj = intids.queryObject(rel.from_id)

            if obj is not None and checkPermission('zope2.View', obj):
                result.append(obj)

        return result

    def relationships_object(self):
        # Get relationships where person or organization is the object

        """
        Return back references from source object on specified attribute_name
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context

        result = []

        for rel in catalog.findRelations(
            dict(to_id=intids.getId(aq_inner(source_object)),
                 from_attribute='relationship_object')
              ):

            obj = intids.queryObject(rel.from_id)

            if obj is not None and checkPermission('zope2.View', obj):
                result.append(obj)

        return result


    def relationship_title(self, value):

        factory = getUtility(IVocabularyFactory,
                             'popolo.contenttypes.relationshiptypes')

        vocabulary = factory(self)

        term = vocabulary.getTerm(value)

        return term.title
