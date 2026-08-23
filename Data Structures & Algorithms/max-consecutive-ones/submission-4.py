class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = best = 0
        for i in nums:
            if i == 1:
                current += 1
            else: 
                current = 0
            if best < current:
                best = current
        return best
        