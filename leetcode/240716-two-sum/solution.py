from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums[index1+1:], start=index1+1):
                print(index2, num2)
                if num1 + num2 == target:
                    return [index1, index2]
