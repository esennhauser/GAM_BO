Feature: log out GAM with multiple users
  As a test automation engineer,
  I want to be able to log out from GAM

  Background: GAM 2.0 BO dev environment
              I am on the Log in Page
  Given we launch browser and go to GAM

  Scenario Outline:  We log out with all types of users
    When we login with "<username>" and "<password>"
    Then Bienvenido is at the top corner
    Then we log out
    And  I am in log in page again

    Examples: Error messages
      |         username               |      password     |
      | administrative@test.com        | g4mr3n0v4c10n     |
      | client@test.com                | g4mr3n0v4c10n     |
      | ecommerce@test.com             | g4mr3n0v4c10n     |
      | general_administrator@test.com | g4mr3n0v4c10n     |
      | logistic@test.com              | g4mr3n0v4c10n     |
      | manager_gba@test.com           | g4mr3n0v4c10n     |
      | manager_zonal@test.com         | g4mr3n0v4c10n     |
      | staff@test.com                 | g4mr3n0v4c10n     |
      | admin@guialemor.com            | g4mr3n0v4c10n     |