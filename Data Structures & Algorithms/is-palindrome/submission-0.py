class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for st in s:
            if st.isalnum():
                newStr = newStr + st.lower()
                
        revStr = newStr[::-1] 
        return revStr == newStr
