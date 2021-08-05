# -*- coding: utf-8 -*-

from plone.app.z3cform import converters
import six

"""
Patch for searching and adding resources #14
https://github.com/Sinar/popolo.contenttypes/issues/14  

Back porting plone.app.z3cform commit
https://github.com/plone/plone.app.z3cform/commit/cb890dbbe64dc92acd2c68d5315f22c32ac4513f

We overload the 'toWidgetValue' and toFieldValue from plone.app.z3cform 3.2.x version.  
"""

def toWidgetValue(self, value):
    """Converts from field value to widget tokenized widget value.
    :param value: Field value.
    :type value: list |tuple | set
    :returns: Items separated using separator defined on widget
    :rtype: string
    """
    if not value:
        return self.field.missing_value
    vocabulary = self.widget.get_vocabulary()
    tokenized_value = []
    for term_value in value:
        if vocabulary is not None:
            try:
                term = vocabulary.getTerm(term_value)
                tokenized_value.append(term.token)
                continue
            except (LookupError, ValueError):
                pass
        tokenized_value.append(six.text_type(term_value))
    return getattr(self.widget, 'separator', ';').join(tokenized_value)



def toFieldValue(self, value):
    """Converts from widget value to field.
    :param value: Value inserted by AjaxSelect widget.
    :type value: string
    :returns: List of items
    :rtype: list | tuple | set
    """
    collectionType = self.field._type
    if isinstance(collectionType, tuple):
        collectionType = collectionType[-1]
    if not len(value):
        return self.field.missing_value
    valueType = self.field.value_type._type
    if isinstance(valueType, tuple):
        valueType = valueType[0]
    separator = getattr(self.widget, 'separator', ';')
    self.widget.update()  # needed to have a vocabulary
    vocabulary = self.widget.get_vocabulary()
    untokenized_value = []
    for token in value.split(separator):
        if vocabulary is not None:
            try:
                term = vocabulary.getTermByToken(token)
                if valueType:
                    untokenized_value.append(valueType(term.value))
                else:
                    untokenized_value.append(term.value)
                continue
            except (LookupError, ValueError):
                pass
        untokenized_value.append(
            valueType(token) if valueType else token,
        )
    return collectionType(untokenized_value)
