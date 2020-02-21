Feature: Navigate through reddit
    Browse favorite subreddits

    Scenario: Navigate to r_all
        When I click on r_all
        Then I am on r_all

     @sub
     Scenario: Navigate to subreddit
        Given I have the following <subreddit> subreddit
        When I click on <subreddit> subreddit
        Then I navigate to <subreddit> subreddit

        Examples:
            | subreddit |
            | AskReddit |
            | funny     |

    @home
     Scenario: Clicking on the header image on the banner sends you to the home page
        Given I have the following <subreddit> subreddit
        When I click on <subreddit> subreddit
        Then I navigate to <subreddit> subreddit
        Then I click on the header image
        Then I am on the home page

        Examples:
            | subreddit |
            | news    |
            | aww       |