class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for i in range(len(emails)):
            cleaned_email = emails[i].split("@")[0].split("+")[0].replace(".","")
            seen.add(cleaned_email + "@" + emails[i].split("@")[1])
        return len(seen)
        