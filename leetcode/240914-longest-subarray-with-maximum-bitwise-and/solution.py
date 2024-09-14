def longestSubarray(nums):
        max_val = max(nums)
    
        longest = 0
        current_length = 0
        
        for num in nums:
            if num == max_val:
                current_length += 1
                longest = max(longest, current_length)
            else:
                current_length = 0
                
        return longest