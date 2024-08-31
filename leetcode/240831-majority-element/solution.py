from typing import List

def majorityElement(nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > len(nums) // 2:
                return num
        return None