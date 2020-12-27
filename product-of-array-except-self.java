/**
 Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
 */

/**
 * 
 * SOLUTIONS:
 * 
 * Approach 1: We maintain two arrays L and R where we store the values of all
 * elements multiplied on the left and right side at that particular index. We
 * can then calculate the A[i] = L[i]*R[i]
 * 
 * Approach 2: This aproach uses only a singular array and is what is
 * implemented in the code below. The resultant array is looped through twice
 * once to calculate the product of elements to the left of A[i] and then
 * another in the reverse direction to calculate the right side on the fly.
 * 
 */

class Solution {
	public int[] productExceptSelf(int[] nums) {
		int l = nums.length;
		int[] res = new int[l];
		res[0] = 1;
		for (int i = 1; i < l; i++) {
			res[i] = res[i - 1] * nums[i - 1];
		}
		int r = 1;
		for (int i = l - 1; i >= 0; i--) {
			res[i] = res[i] * r;
			r *= nums[i];
		}

		return res;
	}
}
