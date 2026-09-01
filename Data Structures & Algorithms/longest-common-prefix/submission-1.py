class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = strs[0]
        for i in range(len(strs)):
            for c in range(min(len(res),len(strs[i]))):
                if strs[i][c] != res[c]:
                    res = res[:c]
                    break
            if len(strs[i]) < len(res):
                res = res[:len(strs[i])]
        return res
        

    

            


        