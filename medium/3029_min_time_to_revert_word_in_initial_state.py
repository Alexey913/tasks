# You are given a 0-indexed string word and an integer k.

# At every second, you must perform the following operations:

# Remove the first k characters of word.
# Add any k characters to the end of word.
# Note that you do not necessarily need to add the same
# characters that you removed. However, you must perform
# both operations at every second.

# Return the minimum time greater than zero required
# for word to revert to its initial state.


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        l = len(word)
        if k == l:
            return 1
        seconds = 1
        for i in range(k,l,k):
            if word[:l-i] == word[i:]:
                return seconds
            seconds += 1
        return seconds