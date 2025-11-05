class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s

        start, end = 0, 0  # indices for the longest palindrome found

        def expandAroundCenter(left, right):
            # Expand while within bounds and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return length of palindrome and its bounds
            return right - left - 1, left + 1, right - 1

        for i in range(len(s)):
            len1, l1, r1 = expandAroundCenter(i, i)       # odd-length palindrome
            len2, l2, r2 = expandAroundCenter(i, i + 1)   # even-length palindrome

            # choose the longer palindrome
            if len1 > (end - start):
                start, end = l1, r1
            if len2 > (end - start):
                start, end = l2, r2

        return s[start:end + 1]
