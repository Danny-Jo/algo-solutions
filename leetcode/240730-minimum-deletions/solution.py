def minimumDeletions(s: str) -> int:
    total_a = s.count('a')
    left_b = 0
    right_a = total_a
    min_deletions = float('inf')
        
    for char in s:
        if char == 'a':
            right_a -= 1
        min_deletions = min(min_deletions, left_b + right_a)
        if char == 'b':
            left_b += 1
        
    return min_deletions