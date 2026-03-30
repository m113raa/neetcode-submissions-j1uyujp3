from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashS = {}
        for i in nums:
            if i in hashS:
                return True
            hashS[i] = 1
        return False
