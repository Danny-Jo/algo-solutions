from typing import List

def kthDistinct2(arr: List[str], k: int) -> str:
        distinct_arr={} # 빈 딕셔너리 생성
        for i in arr:
            if i in distinct_arr:
                distinct_arr[i]+=1 # i라는 key에 value값을 +1
            else:
                distinct_arr[i]=1 # i라는 key에 value 초기값을 1로 설정
        n=0
        for key,value in distinct_arr.items():
            if value==1:
                n+=1
            if n==k:
                return key
        return ""