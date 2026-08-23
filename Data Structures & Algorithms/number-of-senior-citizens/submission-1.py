class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for i in range(len(details)):
            detail = details[i]
            check = detail[11:13]
            if (check > '60'):
                res += 1
        return res


        