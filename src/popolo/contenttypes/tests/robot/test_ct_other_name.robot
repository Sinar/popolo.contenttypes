# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s popolo.contenttypes -t test_other_name.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src popolo.contenttypes.testing.POPOLO_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/popolo/contenttypes/tests/robot/test_other_name.robot
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

Scenario: As a site administrator I can add a Other Name
  Given a logged-in site administrator
    and an add Person form
   When I type 'My Other Name' into the title field
    and I submit the form
   Then a Other Name with the title 'My Other Name' has been created

Scenario: As a site administrator I can view a Other Name
  Given a logged-in site administrator
    and a Other Name 'My Other Name'
   When I go to the Other Name view
   Then I can see the Other Name title 'My Other Name'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Person form
  Go To  ${PLONE_URL}/++add++Person

a Other Name 'My Other Name'
  Create content  type=Person  id=my-other_name  title=My Other Name

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Other Name view
  Go To  ${PLONE_URL}/my-other_name
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Other Name with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Other Name title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
