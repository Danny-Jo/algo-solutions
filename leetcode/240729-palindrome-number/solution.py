def isPalindrome(x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]