from typing import List

def maxDistance(arrays: List[List[int]]) -> int:
        result = 0
        min_first = arrays[0][0]
        max_last = arrays[0][-1]
        
        for i in range(1, len(arrays)):
            current_first = arrays[i][0]
            current_last = arrays[i][-1]
            
            result = max(result, abs(current_last - min_first), abs(max_last - current_first))
            
            min_first = min(min_first, current_first)
            max_last = max(max_last, current_last)
        
        return result