Feature: failing to login GAM
  As a test automation engineer,
  I want to receive information about why
  I am not being able to login.

  Background: GAM 2.0 BO dev environment
              I am on the Log in Page

  Scenario Outline:  Invalid Login
    Given we launch browser and go to GAM
    When we login with "<username>" and "<password>"
    Then The error message is: "<error_message>"

    Examples: Error messages
      | username            | password     | error_message                             |
      | ernesto             | password123  | Email or Password is invalid              |
      |      ''             | password123  | username must be at least 6 characters    |
      | ernesto             |       ''     | password must be at least 6 characters    |
      |       ''            |       ''     | username must be at least 6 characters    |
      | admin@guialemor.com | password123  | Email or Password is invalid              |