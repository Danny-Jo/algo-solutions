def stoneGameII(piles):
    n = len(piles)
    
    memo = {}
    
    def dp(i, m):
        if i >= n:
            return 0
        
        if (i, m) in memo:
            return memo[(i, m)]
        
        total_stones = sum(piles[i:])
        
        max_stones = 0
        current_sum = 0
        
        for x in range(1, 2 * m + 1):
            if i + x > n:  
                break
            current_sum += piles[i + x - 1]
            max_stones = max(max_stones, current_sum + (total_stones - current_sum) - dp(i + x, max(m, x)))
        
        memo[(i, m)] = max_stones
        return max_stones
    
    return dp(0, 1)