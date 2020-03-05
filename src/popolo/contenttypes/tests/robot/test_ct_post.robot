# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s popolo.contenttypes -t test_post.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src popolo.contenttypes.testing.POPOLO_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/popolo/contenttypes/tests/robot/test_post.robot
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

Scenario: As a site administrator I can add a Post
  Given a logged-in site administrator
    and an add Organization form
   When I type 'My Post' into the title field
    and I submit the form
   Then a Post with the title 'My Post' has been created

Scenario: As a site administrator I can view a Post
  Given a logged-in site administrator
    and a Post 'My Post'
   When I go to the Post view
   Then I can see the Post title 'My Post'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Organization form
  Go To  ${PLONE_URL}/++add++Organization

a Post 'My Post'
  Create content  type=Organization  id=my-post  title=My Post

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Post view
  Go To  ${PLONE_URL}/my-post
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Post with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Post title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
