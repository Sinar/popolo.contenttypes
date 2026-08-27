from zc.relation.interfaces import ICatalog
from zope.component import getUtility
from zope.component import queryUtility

from zope.intid.interfaces import IIntIds
from plone.app.linkintegrity.handlers import referencedRelationship

def get_relations(obj, attribute=None, backrefs=False):
    """Get any kind of references and backreferences"""
    int_id = get_intid(obj)
    if not int_id:
        return retval

    relation_catalog = getUtility(ICatalog)
    if not relation_catalog:
        return retval

    query = {}
    if attribute:
        # Constrain the search for certain relation-types.
        query['from_attribute'] = attribute

    if backrefs:
        query['to_id'] = int_id
    else:
        query['from_id'] = int_id

    return relation_catalog.findRelations(query)


def get_backrelations(obj, attribute=None):
    return get_relations(obj, attribute=attribute, backrefs=True)


def get_intid(obj):
    """Return the intid of an object from the intid-catalog"""
    intids = queryUtility(IIntIds)
    if intids is None:
        return
    # check that the object has an intid, otherwise there's nothing to be done
    try:
        return intids.getId(obj)
    except KeyError:
        # The object has not been added to the ZODB yet
        return
