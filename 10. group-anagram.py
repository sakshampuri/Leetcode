import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = collections.defaultdict(list)
        for s in strs:
            out[tuple(sorted(s))].append(s)
        return out.values()