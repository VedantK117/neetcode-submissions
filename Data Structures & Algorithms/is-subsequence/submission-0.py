class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        n = len(s)
        m = len(t)
        if n==0:
            return True
        if m==0:
            return False
        while(i<=n and j<=m):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
            if i==n: 
                return True
            if j==m:
                return False
                        
        