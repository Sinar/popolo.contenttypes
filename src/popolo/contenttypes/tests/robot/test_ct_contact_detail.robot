# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s popolo.contenttypes -t test_contact_detail.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src popolo.contenttypes.testing.POPOLO_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/popolo/contenttypes/tests/robot/test_contact_detail.robot
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

Scenario: As a site administrator I can add a Contact Detail
  Given a logged-in site administrator
    and an add Person form
   When I type 'My Contact Detail' into the title field
    and I submit the form
   Then a Contact Detail with the title 'My Contact Detail' has been created

Scenario: As a site administrator I can view a Contact Detail
  Given a logged-in site administrator
    and a Contact Detail 'My Contact Detail'
   When I go to the Contact Detail view
   Then I can see the Contact Detail title 'My Contact Detail'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Person form
  Go To  ${PLONE_URL}/++add++Person

a Contact Detail 'My Contact Detail'
  Create content  type=Person  id=my-contact_detail  title=My Contact Detail

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Contact Detail view
  Go To  ${PLONE_URL}/my-contact_detail
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Contact Detail with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Contact Detail title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
