# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s popolo.contenttypes -t test_source.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src popolo.contenttypes.testing.POPOLO_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/popolo/contenttypes/tests/robot/test_source.robot
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

Scenario: As a site administrator I can add a Source
  Given a logged-in site administrator
    and an add Contact_Detail form
   When I type 'My Source' into the title field
    and I submit the form
   Then a Source with the title 'My Source' has been created

Scenario: As a site administrator I can view a Source
  Given a logged-in site administrator
    and a Source 'My Source'
   When I go to the Source view
   Then I can see the Source title 'My Source'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Contact_Detail form
  Go To  ${PLONE_URL}/++add++Contact_Detail

a Source 'My Source'
  Create content  type=Contact_Detail  id=my-source  title=My Source

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Source view
  Go To  ${PLONE_URL}/my-source
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Source with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Source title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
