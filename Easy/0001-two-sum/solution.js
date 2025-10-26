/**
 * LeetCode Problem #1: Two Sum
 * Difficulty: Easy
 * 
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
var twoSum = function(nums, target) {
    // Hash map to store: number -> index
    const seen = new Map();
    
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        
        // Check if complement exists in hash map
        if (seen.has(complement)) {
            return [seen.get(complement), i];
        }
        
        // Store current number and its index
        seen.set(nums[i], i);
    }
    
    // Should never reach here based on problem constraints
    return [];
};


// Alternative Solution: Brute Force
var twoSumBruteForce = function(nums, target) {
    const n = nums.length;
    
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }
    
    return [];
};


// Test cases
console.log('Test 1:', JSON.stringify(twoSum([2, 7, 11, 15], 9))); // [0, 1]
console.log('Test 2:', JSON.stringify(twoSum([3, 2, 4], 6)));      // [1, 2]
console.log('Test 3:', JSON.stringify(twoSum([3, 3], 6)));         // [0, 1]
console.log('✅ All tests completed!');
