class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1 = {}
        c2 = {}
        for char in s:
            if char in c1:
                c1[char]+=1
                continue
            c1[char]=0
        for char in t:
            if char in c2:
                c2[char]+=1
                continue
            c2[char]=0
        return c1 == c2
        