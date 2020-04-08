# -*- coding: utf-8 -*-

# from popolo.contenttypes import _
from plone.dexterity.browser.view import DefaultView

# import popolo.contenttypes.utils as utils


from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
# from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class PersonView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('person_view.pt')

    def __call__(self):
        # Implement your own actions:
        return super(PersonView, self).__call__()


    def memberships(self):
        """
        Return back references from source object on specified attribute_name
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        attribute_name = 'person'

        result = []

        for rel in catalog.findRelations(
            dict(to_id=intids.getId(aq_inner(source_object)),
                                    from_attribute=attribute_name)
              ):
           
            obj = intids.queryObject(rel.from_id)

            if obj is not None and checkPermission('zope2.View', obj):
                if obj.portal_type == 'Membership':
                    result.append(obj)

        return result

    def implicated(self):
        """
        Return back references from source object on specified attribute_name
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        attribute_name = 'implicated'

        result = []

        for rel in catalog.findRelations(
            dict(to_id=intids.getId(aq_inner(source_object)),
                                    from_attribute=attribute_name)
              ):
           
            obj = intids.queryObject(rel.from_id)

            if obj is not None and checkPermission('zope2.View', obj):
                result.append(obj)

        return result
