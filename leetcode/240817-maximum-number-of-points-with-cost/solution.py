from typing import List

def maxPoints(points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
    
        dp = points[0][:]
        
        for r in range(1, m):
            new_dp = [0] * n
            
            left_max = dp[0]
            for c in range(n):
                left_max = max(left_max, dp[c] + c)
                new_dp[c] = left_max + points[r][c] - c
            
            right_max = dp[n - 1] - (n - 1)
            for c in range(n - 1, -1, -1):
                right_max = max(right_max, dp[c] - c)
                new_dp[c] = max(new_dp[c], right_max + points[r][c] + c)
            
            dp = new_dp
        
        return max(dp)