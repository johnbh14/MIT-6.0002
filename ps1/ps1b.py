###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    

    #bottom-up tabulation
    for egg_weight in egg_weights:
        memo[egg_weight] = 1
    
    for weight in range(min(egg_weights) + 1, target_weight + 1):
        new_eggs = []
        for egg_weight in egg_weights:
            partial_weight = weight - egg_weight
            if partial_weight > 0:
                new_eggs.append(memo[partial_weight] + 1)
        memo[weight] = min(new_eggs)
    return memo[target_weight]


    """
    #top-down recursion
    if target_weight == 0:
        return 0
    
    if target_weight in memo:
        return memo[target_weight]

    eggs = [] #a list of my solutions for each egg_weight
    
    for egg_weight in egg_weights:
        if egg_weight <= target_weight:
            eggs.append(dp_make_weight(egg_weights, target_weight - egg_weight, memo) + 1)
    
    memo[target_weight] = min(eggs)
    
    return memo[target_weight]
    """

    #Greedy Solution
    """
    egg_weights = sorted(egg_weights, reverse=True)

    eggs_used = 0
    
    for egg_weight in egg_weights:
        num_eggs = target_weight // egg_weight
        target_weight -= num_eggs * egg_weight
        eggs_used += num_eggs

    return eggs_used
    """

    
# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    """
    egg_weights = (1, 3, 7, 13)
    n = 72
    print(egg_weights)
    print(str(n))
    print("Expected ouput: 6 (5 * 13 + 1 * 7 = 72)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
    """
