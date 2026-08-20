class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        right_max = -1
        result = [0] * n 
        for i in range(n-1, -1, -1):
            result[i] = right_max
            right_max = max(right_max,arr[i])
        return result


            

        