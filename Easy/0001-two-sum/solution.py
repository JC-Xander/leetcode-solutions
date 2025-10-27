from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
        
        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    
    # Test 2
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    
    # Test 3
    assert solution.twoSum([3, 3], 6) == [0, 1]
