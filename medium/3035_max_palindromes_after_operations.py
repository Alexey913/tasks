# You are given a 0-indexed string array words having length n
# and containing 0-indexed strings.

# You are allowed to perform the following operation any number
# of times (including zero):

# Choose integers i, j, x, and y such that
# 0 <= i, j < n, 0 <= x < words[i].length, 0 <= y < words[j].length,
# and swap the characters words[i][x] and words[j][y].
# Return an integer denoting the maximum number of palindromes
# words can contain, after performing some operations.

# Note: i and j may be equal during an operation.

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        char_count = [0] * 26
        for word in words:
            for ch in word:
                char_count[ord(ch) - ord('a')] += 1
        pairs_of_char = 0
        for c in char_count:
            pairs_of_char += c // 2
        words.sort(key = len)
        result = 0
        for word in words:
            need_pairs = len(word) // 2
            if pairs_of_char >= need_pairs:
                pairs_of_char -= need_pairs
                result += 1
        return result