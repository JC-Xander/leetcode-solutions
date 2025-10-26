# 1. Two Sum

**Difficulty:** Easy  
**Topics:** Array, Hash Table  
**Link:** [LeetCode Problem](https://leetcode.com/problems/two-sum/)

---

## 📝 Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

### Examples

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

### Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

---

## 💡 Approach

### Method 1: Hash Map (Optimal)

Use a hash map to store the numbers we've seen so far and their indices. For each number, check if `target - current_number` exists in the hash map.

**Algorithm:**
1. Create an empty hash map
2. Iterate through the array
3. For each element, calculate `complement = target - nums[i]`
4. If complement exists in hash map, return `[hash_map[complement], i]`
5. Otherwise, add current number and its index to hash map

---

## ⏱️ Complexity Analysis

### Hash Map Solution
- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(n) - Hash map stores up to n elements

### Brute Force (Alternative)
- **Time Complexity:** O(n²) - Nested loops
- **Space Complexity:** O(1) - No extra space needed

---

## 🔍 Key Insights

- Hash map trades space for time efficiency
- Perfect use case for "looking for complement" pattern
- Remember to check if complement exists BEFORE adding current element (to avoid using same element twice)

---

## 📊 Test Cases

```python
# Test Case 1: Regular case
assert twoSum([2,7,11,15], 9) == [0,1]

# Test Case 2: Numbers not sorted
assert twoSum([3,2,4], 6) == [1,2]

# Test Case 3: Duplicate numbers
assert twoSum([3,3], 6) == [0,1]

# Test Case 4: Negative numbers
assert twoSum([-1,-2,-3,-4,-5], -8) == [2,4]
```

---

## 🏷️ Tags

`#Array` `#HashTable` `#TwoPointer` `#Easy`
