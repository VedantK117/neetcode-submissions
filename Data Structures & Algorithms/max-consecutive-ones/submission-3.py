class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        best = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            else: 
                current = 0
            if best < current:
                best = current
        return best
        