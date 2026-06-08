class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        s = s.upper()
        while i<j:
            if not ( 'A'<=s[i]<='Z' or '0'<=s[i]<='9'):
                i+=1
                continue
            if not ( 'A'<=s[j]<='Z' or '0'<=s[j]<='9'):
                j-=1
                continue
            if s[i] != s[j]:
                print(s[i],s[j])
                return False
            i+=1
            j-=1
        return True