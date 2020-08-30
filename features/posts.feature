Feature: To click on subreddit posts
  View the posts
  Comment on a post
  Create a post
  Delete a post

  Scenario Outline: View a subreddit post
    Given I have the following <subreddit> subreddit
    When I click on <subreddit> subreddit
    Then I navigate to <subreddit> subreddit
    Then I click on a post
    Then I view the post

    Examples:
      | subreddit |
      | AskReddit |