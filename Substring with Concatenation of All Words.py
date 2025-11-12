class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = {}

        # Count frequency of each word in words
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1

        res = []

        # We only need to check starting positions up to word_len
        for i in range(word_len):
            left = i
            seen = {}
            count = 0

            for j in range(i, len(s) - word_len + 1, word_len):
                w = s[j:j + word_len]

                if w in word_count:
                    seen[w] = seen.get(w, 0) + 1
                    count += 1

                    # If a word is seen more times than allowed, shift the window
                    while seen[w] > word_count[w]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # If all words matched
                    if count == num_words:
                        res.append(left)
                else:
                    # Reset window
                    seen.clear()
                    count = 0
                    left = j + word_len

        return res
