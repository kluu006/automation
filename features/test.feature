Feature: Navigate through reddit
    Browse favorite subreddits

    Scenario: Navigate to r_all
        When I click on r_all
        Then I navigate to r_all

     @sub
     Scenario: Navigate to subreddit
        Given I have the following <subreddit>
        When I click on <subreddit>
        Then I navigate to <subreddit>

        Examples:
            | subreddit |
            | AskReddit |
            | funny     |

