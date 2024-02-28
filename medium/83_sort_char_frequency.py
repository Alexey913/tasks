# Given a string s, sort it in decreasing order based
# on the frequency of the characters. The frequency of a character
# is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers,
# return any of them.

from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        sort_dict = defaultdict(int)
        for ch in s:
            sort_dict[ch] += 1
        output = []
        for k, v in sorted(sort_dict.items(), key=lambda x: x[1], reverse=True):
            output.append(k * v)
        return "".join(output)