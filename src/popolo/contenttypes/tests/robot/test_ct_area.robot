# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s popolo.contenttypes -t test_area.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src popolo.contenttypes.testing.POPOLO_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/popolo/contenttypes/tests/robot/test_area.robot
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

Scenario: As a site administrator I can add a Area
  Given a logged-in site administrator
    and an add Area form
   When I type 'My Area' into the title field
    and I submit the form
   Then a Area with the title 'My Area' has been created

Scenario: As a site administrator I can view a Area
  Given a logged-in site administrator
    and a Area 'My Area'
   When I go to the Area view
   Then I can see the Area title 'My Area'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Area form
  Go To  ${PLONE_URL}/++add++Area

a Area 'My Area'
  Create content  type=Area  id=my-area  title=My Area

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Area view
  Go To  ${PLONE_URL}/my-area
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Area with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Area title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
