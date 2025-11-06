# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money. Return the fewest
# number of coins that you need to make up that amount. If that amount of money cannot be made
# up by any combination of the coins, return −1.


# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1


#Understand:

#Similar to Rod Optimization Problem
#Minimization the number of coins
#Edge case: if amount cannot be made up by combs., return -1

#Test Cases: 
# [3,4,7], amount = 24 -> O: 4
# [1,4,2], amount = 8 -> O: 2

#Time Complexity: O(2^n)


#Implementation:
def coinChange(coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')   
        q = float('inf')
        for coin in coins:
            result = coinChange(coins, amount - coin)
            if result != float('inf'):
                q = min(q, 1 + result)
        if q != float('inf'):
            return q
        else: return -1


#Test Cases:

l1 = [1,2,5] 
amount1 = 11
print(coinChange(l1,amount1))  #--> 3

l2 = [1,4,2]
amount2 = 8
print(coinChange(l2,amount2))  #--> 2



        

        

        
        