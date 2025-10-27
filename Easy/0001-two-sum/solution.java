import java.util.HashMap;
import java.util.Map;

public class Solution {

	public int[] twoSum(int[] nums, int target) {

		Map<Integer, Integer> see = new HashMap<>();

		for (int i = 0; i < nums.length; i++) {
			int complement = target - nums[i];
			
			if (see.containsKey(complement)) {
				return new int[] {see.get(complement), i};
			}
			
			see.put(nums[i], i);
		}

		return  new int[] {};
	}
}