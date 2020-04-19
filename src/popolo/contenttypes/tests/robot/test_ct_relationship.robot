# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s popolo.contenttypes -t test_relationship.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src popolo.contenttypes.testing.POPOLO_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/popolo/contenttypes/tests/robot/test_relationship.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Relationship
  Given a logged-in site administrator
    and an add Person form
   When I type 'My Relationship' into the title field
    and I submit the form
   Then a Relationship with the title 'My Relationship' has been created

Scenario: As a site administrator I can view a Relationship
  Given a logged-in site administrator
    and a Relationship 'My Relationship'
   When I go to the Relationship view
   Then I can see the Relationship title 'My Relationship'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Person form
  Go To  ${PLONE_URL}/++add++Person

a Relationship 'My Relationship'
  Create content  type=Person  id=my-relationship  title=My Relationship

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Relationship view
  Go To  ${PLONE_URL}/my-relationship
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Relationship with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Relationship title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
