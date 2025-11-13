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

#Time Complexity: O(amount * len(coins))


#Implementation:
def coinChange(coins, amount):

    dp = []

    for k in range(0, amount+1):
        dp.append(float('inf'))

    dp[0] = 0

    for j in range(1, amount+1):
        for coin in coins:
            if coin <= j:
                dp[j] = min(dp[j], 1 + dp[j - coin])
        

    if dp[amount] != float('inf'):
        return dp[amount]
    
    else:
        return -1
    

    
    """
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
        else: return -1"""

    


#Test Cases:

l1 = [1,2,5] 
amount1 = 11
print(coinChange(l1,amount1))  #--> 3

l2 = [1,4,2]
amount2 = 8
print(coinChange(l2,amount2))  #--> 2








