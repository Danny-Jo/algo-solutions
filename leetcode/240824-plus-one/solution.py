from typing import List

def plusOne(digits: List[int]) -> List[int]:
        combined_str = ''.join(map(str, digits))
        
        combined_int = int(combined_str)
        
        incremented_int = combined_int + 1
        
        result_array = [int(digit) for digit in str(incremented_int)]
        
        return result_array