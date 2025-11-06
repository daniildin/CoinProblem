# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money. Return the fewest
# number of coins that you need to make up that amount. If that amount of money cannot be made
# up by any combination of the coins, return −1.


# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1


#Understand:

#Similar to Rod Optimization Problem
#Edge case: if amount cannot be made up by combs., return -1

#Test Cases: 
# [3,4,7], amount = 24 -> O: 4
# [1,4,2], amount = 8 -> O: 2


#Plan: 

#