# -*- coding: utf-8 -*-

from popolo.contenttypes import _
from plone.dexterity.browser.view import DefaultView
from zope.component import getMultiAdapter

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class SourceView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('source_view.pt')

    def __call__(self):
        # Implement your own actions:
        return super(SourceView, self).__call__()
