# -*- coding: utf-8 -*-

from plone import api
from popolo.contenttypes import _
from Products.Five.browser import BrowserView
from plone.dexterity.browser.view import DefaultView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class OrganizationView(DefaultView,BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('organization_view.pt')

    def boo(self):
        text = u'Boo'
        return text
