class Solution:
    from collections import deque
    def isValid(self, s: str) -> bool:
        stack = deque(maxlen=(10**4)//2)
        push = {char:True for char in '{[('}
        pop = {'{':'}','[':']','(':')'}
        for char in s:
            if char in push:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if pop[stack.pop()] != char:
                    return False
        return len(stack) == 0
        