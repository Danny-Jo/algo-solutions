from typing import List

def kthDistinct(arr: List[str], k: int) -> str:
        distinct_arr = []
        duplication_arr = []

        for i in arr:
            if i not in distinct_arr and i not in duplication_arr:
                distinct_arr.append(i)
            else:
                duplication_arr.append(i)
                distinct_arr = list(filter(lambda x: x != i, distinct_arr))

        if k <= len(distinct_arr):
            return distinct_arr[k-1]
        else:
            return ""