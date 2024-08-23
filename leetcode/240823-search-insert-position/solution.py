from typing import List

def searchInsert(nums: List[int], target: int) -> int:
        for i, v in enumerate(nums):
            if v >= target:
                return i
        return len(nums)