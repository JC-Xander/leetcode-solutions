"""
LeetCode Problem #1: Two Sum
Difficulty: Easy
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two indices where nums[i] + nums[j] = target
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List containing two indices [i, j]
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Hash map to store: number -> index
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in hash map
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number and its index
            seen[num] = i
        
        # Should never reach here based on problem constraints
        return []


# Alternative Solution: Brute Force
class SolutionBruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force approach using nested loops
        
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    print("✅ Test 1 passed")
    
    # Test 2
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    print("✅ Test 2 passed")
    
    # Test 3
    assert solution.twoSum([3, 3], 6) == [0, 1]
    print("✅ Test 3 passed")
    
    print("\n🎉 All tests passed!")
