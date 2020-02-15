Feature: Navigate through reddit
    Browse favorite subreddits

    Scenario: Navigate to r_all
        Given I am on reddit
        When I click on r_all
        Then I navigate to r_all
