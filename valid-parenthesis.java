
/**
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 **/
import java.util.*;

class Solution {

	private HashMap<Character, Character> map;

	Solution() {

		// Initialising the hashmap to contain all the corresponding opening brackets
		// We need to check whether the particular closing bracket corresponds to the
		// opening bracket in front of the stack (deque) hence the preference for the
		// closing bracket as the keys
		// The implementation, however, can just as easily be done the other way around
		this.map = new HashMap<Character, Character>();
		this.map.put(')', '(');
		this.map.put('}', '{');
		this.map.put(']', '[');
	}

	public boolean isValid(String s) {

		// Deque is used instead of legacy Stack implementation
		Deque<Character> stack = new ArrayDeque<Character>();

		// Iterating through all characters using advanced for loop
		for (char c : s.toCharArray()) {

			// Checking if the current character is closing
			if (map.containsKey(c)) {
				// Since the current character is closing, we'll check if the stack
				// contains the corresponding opening bracket
				if (!stack.isEmpty() && stack.peekFirst() == map.get(c))
					stack.removeFirst();
				else
					return false;
			}
			// Means bracket is opening
			else {
				// Simply pushing it on to the stack
				stack.addFirst(c);
			}
		}

		return stack.isEmpty();
	}
}
