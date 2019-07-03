class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        # write your code here
        if not s: return True
        i = 0
        j = len(s) - 1
        while i < j:
            while not s[i].isalnum(): i += 1
            while not s[j].isalnum(): j -= 1
            if i >= j: break
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        return True

sol = Solution()
sol.isPalindrome("A man, a plan, a canal: Panama")