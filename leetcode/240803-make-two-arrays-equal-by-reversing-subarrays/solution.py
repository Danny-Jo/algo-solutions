from typing import List

def canBeEqual(target: List[int], arr: List[int]) -> bool:
    return sorted(target) == sorted(arr)
