Feature: failing to login GAM
  As a test automation engineer,
  I want to receive information about why
  I am not being able to login.

  Background: GAM 2.0 BO dev environment
              I am on the Log in Page

  Scenario:  Wrong Username And Wrong Password
    Given we launch browser and go to GAM
    When we login with 'ernesto' and 'password123'
    Then The error message is: "Email or Password is invalid"

  Scenario:  Empty Username And Wrong Password
    Given we launch browser and go to GAM
    When we login with ' ' and 'password123'
    Then The error message is: "password must be at least 6 characters"

  Scenario:  Wrong Username And Empty Password
    Given we launch browser and go to GAM
    When we login with 'ernesto' and ' '
    Then The error message is: "password must be at least 6 characters"

  Scenario:  Empty Username And Empty Password
    Given we launch browser and go to GAM
    When we login with ' ' and ' '
    Then The error message is: "username must be at least 6 characters"

  Scenario:  Wrong Password
    Given we launch browser and go to GAM
    When we login with 'admin@guialemor.com' and 'password123'
    Then The error message is: "Email or Password is invalid"