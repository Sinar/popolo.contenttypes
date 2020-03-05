# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s popolo.contenttypes -t test_organization.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src popolo.contenttypes.testing.POPOLO_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/popolo/contenttypes/tests/robot/test_organization.robot
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

Scenario: As a site administrator I can add a Organization
  Given a logged-in site administrator
    and an add Organization form
   When I type 'My Organization' into the title field
    and I submit the form
   Then a Organization with the title 'My Organization' has been created

Scenario: As a site administrator I can view a Organization
  Given a logged-in site administrator
    and a Organization 'My Organization'
   When I go to the Organization view
   Then I can see the Organization title 'My Organization'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Organization form
  Go To  ${PLONE_URL}/++add++Organization

a Organization 'My Organization'
  Create content  type=Organization  id=my-organization  title=My Organization

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Organization view
  Go To  ${PLONE_URL}/my-organization
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Organization with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Organization title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
