def addBinary(a: str, b: str) -> str:
    num1 = int(a, 2)
    num2 = int(b, 2)
        
    sum_num = num1 + num2
        
    return bin(sum_num)[2:]