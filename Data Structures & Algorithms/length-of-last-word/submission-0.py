class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        s = s.rstrip()
        for i in range(len(s) -1,-1,-1):
            if s[i] == " ":
                return res
            else: res += 1
        return res
            

        