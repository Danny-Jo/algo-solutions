def minSwaps(nums: List[int]) -> int:
        total_ones = sum(nums)
    
        if total_ones == 0 or total_ones == 1:
            return 0
        
        extended_nums = nums + nums
        n = len(nums)
        min_zeros = float('inf')
        current_zeros = 0
        
        for i in range(total_ones):
            if extended_nums[i] == 0:
                current_zeros += 1

        min_zeros = min(min_zeros, current_zeros)
        
        for i in range(1, n):
            if extended_nums[i - 1] == 0:
                current_zeros -= 1
            if extended_nums[i + total_ones - 1] == 0:
                current_zeros += 1
            min_zeros = min(min_zeros, current_zeros)
        
        return min_zeros