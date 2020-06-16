Feature: AAPL Tests

  Scenario: The endpoint shall return the following KV pairs in order : date, open, high, low, close, adjusted_close, volume
    Given we are connected to AAPL US "https://eodhistoricaldata.com/api/eod/AAPL.US" for dates from "2019-01-01" to "2019-01-04" with "OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX"
    When  we get the data
    Then  we verified the keyvalue pairs "date open high low close adjusted_close volume"


  Scenario: The endpoint shall optionally take &from and &to parameters to limit the range of date that come back to be bounded by these inclusive dates
    Given we are connected to AAPL US "https://eodhistoricaldata.com/api/eod/AAPL.US" for dates from "2019-01-01" to "2019-01-04" with "OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX"
    When  we get the data
    Then  we verify if the all "4" records inclusive of from date to date are present

  Scenario: All calendar dates within the given range must be returned
    Given we are connected to AAPL US "https://eodhistoricaldata.com/api/eod/AAPL.US" for dates from "2019-01-01" to "2019-03-04" with "OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX"
    When  we get the data
    Then  we verify if all calender dates within the given range from "2019-01-01" to "2019-03-04"

  Scenario: No close prices can be zero or negative
    Given we are connected to AAPL US "https://eodhistoricaldata.com/api/eod/AAPL.US" for dates from "2019-01-01" to "2019-03-04" with "OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX"
    When  we get the data
    Then  we verify no close prices can be zero or negative

  Scenario: The high price must always be greater than or equal to the close price
    Given we are connected to AAPL US "https://eodhistoricaldata.com/api/eod/AAPL.US" for dates from "2019-01-01" to "2019-03-04" with "OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX"
    When  we get the data
    Then  we verify that "high" price must always be greater than or equal to "close" price

  Scenario: The low price must always be less than or equal to the close price
    Given we are connected to AAPL US "https://eodhistoricaldata.com/api/eod/AAPL.US" for dates from "2019-01-01" to "2019-03-04" with "OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX"
    When  we get the data
    Then  we verify that "close" price must always be greater than or equal to "low" price