Feature: Log into an account

  Scenario: Log into an account
    Given I have a valid username and password
    When I click the username form and enter username
    Then I click the password form and enter password
    Then I click the login button
    Then I am logged in