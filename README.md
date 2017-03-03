# Porject Title: 2Sigma
This is the project for AI final project

## Overview
The overview of the project requirement

## Description
Finding the perfect place to call your new home should be more than browsing through endless listings. [RentHop](https://www.renthop.com) makes apartment search smarter by using data to sort rental listings by quality. But while looking for the perfect apartment is difficult enough, structuring and making sense of all available real estate data programmatically is even harder. Two [Sigma](https://www.twosigma.com) and RentHop, a portfolio company of Two Sigma Ventures, invite Kagglers to unleash their creative engines to uncover business value in this unique recruiting competition.

Two Sigma invites you to apply your talents in this recruiting competition featuring rental listing data from RentHop. Kagglers will ** predict the number of inquiries a new listing receives based on the listing’s creation date and other features. Doing so will help RentHop better handle fraud control, identify potential listing quality issues, and allow owners and agents to better understand renters’ needs and preferences.**

Two Sigma has been at the forefront of applying technology and data science to financial forecasts. While their pioneering advances in big data, AI, and machine learning in the financial world have been pushing the industry forward, as with all other scientific progress, they are driven to make continual progress. This challenge is an opportunity for competitors to gain a sneak peek into Two Sigma's data science work outside of finance.

## Evaluation
Submissions are evaluated using the multi-class logarithmic loss. Each listing has one true class. For each listing, you must submit a set of predicted probabilities (one for every listing). The formula is then,

### Submitting
You must submit a csv file with the listing_id, and a probability for each class.
The order of the rows does not matter. The file must have a header and should look like the following:
'''
listing_id,high,medium,low
7065104,0.07743170693194379,0.2300252644876046,0.6925430285804516
7089035,0.0, 1.0, 0.0
...
'''

