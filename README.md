# politikus.popolo

Popolo-spec content types for [Plone](https://plone.org) 6.2: persons,
organizations, posts, relationships, and the supporting content types
(identifiers, other names, contact details, memberships, areas, sources).

Part of the [Politikus](https://github.com/Sinar/politikus) project, a CMS
for investigative journalism built on open data standards (Popolo, OCDS,
BODS).

## Content types

- **Person** — a natural person, with relationships, identifiers, other
  names, contact details, sources and memberships
- **Organization** — a legal entity, with founding/dissolution dates,
  classification and contact details
- **Post** — a position held by a person in an organization
- **Relationship** — a typed, dated relationship between persons and/or
  organizations (see `docs/docs/reference/relations.md` for the taxonomy)
- **Membership** — a person's membership in an organization
- **Identifier** — an external identifier (e.g. tax, company registration)
- **Other Name** — an alternate name (e.g. aka, former name)
- **Contact Detail** — phone, email, website, address
- **Area** — a geographic area (linked to GeoNames feature codes)
- **Source** — a source for a claim or relationship

See `docs/docs/reference/relations.md` for the relationship taxonomy.

## Installation

This add-on is developed as a source checkout inside the
[politikus buildout](https://github.com/Sinar/politikus) (mr.developer,
`branch=plone6`). Create a Plone site, then install `politikus.popolo` via
the Plone Add-ons screen.

## Testing

The test suite runs with `zope.testrunner` against a Plone 6.2 egg set:

```shell
zope-testrunner --test-path src -s politikus.popolo \
    -t 'test_(behavior|ct|setup|view|viewlet|vocab)'
```

Robot tests (`tests/robot/*.robot`) need a browser and are excluded from
the fast loop.

Locale catalogs (`locales/`) are updated with the buildout's
`bin/i18n-extract` and `bin/i18n-compile` scripts; compiled `.mo` files are
committed.

## Credits

Generated from the [plonecli](https://github.com/plone/plonecli) `addon`
template (bobtemplates.plone), carrying over the content of the former
`popolo.contenttypes` package.
