class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}  # stores the last index of each character
        left = 0  # left boundary of the current window
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                # move left boundary right after the previous occurrence
                left = char_index[s[right]] + 1

            char_index[s[right]] = right  # update the last index
            max_len = max(max_len, right - left + 1)

        return max_len
