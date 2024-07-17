def longestPalindrome1(s: str) -> str:
    if len(s) == 1:
        return s
        
    answer = ''
    for i, c1 in enumerate(s):
        for j, c2 in enumerate(s[i+1:], start=i+1):
            if i == 0:
                if s[i:j+1] == s[j::-1]:
                    if len(answer) < len(s[j::-1]):
                        answer = s[j::-1]
            else:
                if s[i:j+1] == s[j:i-1:-1]: 
                    if len(answer) < len(s[j:i-1:-1]):
                        answer = s[j:i-1:-1]
    return answer

def longestPalindrome2(s: str) -> str:
    # * s 자체가 palindrome이면 어차피 제일 크니 바로 반환
    if s == s[::-1]:
        return s
    t, n = 0, 1
    for i in range(1, len(s)):
        l, r = i - n, i + 1
        s1 = s[l-1 : r]
        print("s1: ", s1)
        if l >= 1 and s1 == s1[::-1]:
            n += 2
            t = l - 1
        else:
            s2 = s[l:r]
            if s2 == s2[::-1]:
                n += 1
                t = l
    return s[t:t+n]
