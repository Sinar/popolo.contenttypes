# -*- coding: utf-8 -*-

#from popolo.contenttypes import _
from plone.dexterity.browser.view import DefaultView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

#import popolo.contenttypes.utils as utils

from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


class PostView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('post_view.pt')

    def __call__(self):
        # Implement your own actions:
        return super(PostView, self).__call__()

    def memberships(self):
        """
        Return back references from source object on specified attribute_name
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        attribute_name = 'post'

        result = []

        for rel in catalog.findRelations(
            dict(to_id=intids.getId(aq_inner(source_object)),
                 from_attribute=attribute_name)
              ):
           
            obj = intids.queryObject(rel.from_id)

            if obj is not None and checkPermission('zope2.View', obj):

                # person should be required field, but don't return
                # post memberships without a person
                # https://github.com/Sinar/popolo.contenttypes/issues/14
                if obj.portal_type == 'Membership' and obj.person:
                    result.append(obj)

        return result
