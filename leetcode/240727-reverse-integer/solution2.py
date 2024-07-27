def reverse(x: int) -> int:
    x = str(x)
    x = x[::-1]
    x.lstrip('0')
    if(x[-1]=='-'):
        x = x[:len(x)-1]
        x = '-'+x
    x = int(x)
    if(x < -(2**31) or x > (2**31 -1)):
        return 0
    return x

# * 새로 알게된 점 - python에서 if문을 쓸 때 else를 작성하지 않고 문제를 해결할 수 있으면 속도가 빨라짐. 최대한 else를 사용하지 않고 if문 하나로만 풀기 