# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s popolo.contenttypes -t test_person.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src popolo.contenttypes.testing.POPOLO_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/popolo/contenttypes/tests/robot/test_person.robot
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

Scenario: As a site administrator I can add a Person
  Given a logged-in site administrator
    and an add Person form
   When I type 'My Person' into the title field
    and I submit the form
   Then a Person with the title 'My Person' has been created

Scenario: As a site administrator I can view a Person
  Given a logged-in site administrator
    and a Person 'My Person'
   When I go to the Person view
   Then I can see the Person title 'My Person'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Person form
  Go To  ${PLONE_URL}/++add++Person

a Person 'My Person'
  Create content  type=Person  id=my-person  title=My Person

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Person view
  Go To  ${PLONE_URL}/my-person
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Person with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Person title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
