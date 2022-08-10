Supermarket Receipt
===================

This is supposed to represent a fragment of a larger system used in a supermarket. It contains the code for calculating the price of a shopping cart full of items, including any discounts. The production code in the 'src' folder contains all the business logic. 

You'd like to write tests especially for all the various kinds of discount listed in the enum 'SpecialOfferType'. To get you started, there is a 'test_rig.py' script in the test folder, and a couple more supporting scripts. The test rig can read csv files containing the current product catalog, the special offers, and the shopping cart. It calls the production code then prints the outcome in the form of the receipt.

The TextTest Config file is set up to use this test rig, and we've provided samples of the three kinds of csv files. You should add tests for all the various kinds of discount.
