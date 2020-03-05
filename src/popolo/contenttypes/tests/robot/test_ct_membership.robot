# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s popolo.contenttypes -t test_membership.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src popolo.contenttypes.testing.POPOLO_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/popolo/contenttypes/tests/robot/test_membership.robot
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

Scenario: As a site administrator I can add a Membership
  Given a logged-in site administrator
    and an add Membership form
   When I type 'My Membership' into the title field
    and I submit the form
   Then a Membership with the title 'My Membership' has been created

Scenario: As a site administrator I can view a Membership
  Given a logged-in site administrator
    and a Membership 'My Membership'
   When I go to the Membership view
   Then I can see the Membership title 'My Membership'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Membership form
  Go To  ${PLONE_URL}/++add++Membership

a Membership 'My Membership'
  Create content  type=Membership  id=my-membership  title=My Membership

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Membership view
  Go To  ${PLONE_URL}/my-membership
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Membership with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Membership title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
