# Created by rapid at 7/27/2020
Feature: # Ability of app to add and delete goods to and from bin

  Scenario: # Add and delete goods to/from bin/hw_19_barantsev
    Given Loginpage
    Then Click on the first item from the list 3 times
    Then Click on checkout button and delete all items from the bin

