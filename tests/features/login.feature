Feature: login GAM
  As a test automation engineer,
  I want to log in into GAM 2.0 BO,
  So that I can verify the login functionality.

  Background: GAM 2.0 BO dev environment
    Given: I am on the Log in Page

  Scenario:  login successfully
     Given we launch browser and go to GAM
      When we login with <username> and <password>
      Then Bienvenido is at the top corner