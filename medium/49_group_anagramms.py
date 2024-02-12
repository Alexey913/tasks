# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging
# the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Первое решение (медленное) 
# strs = ["eat","tea","tan","ate","nat","bat"]
# strs = ["","",""]
# output = []
# for word in strs:
#     for i in output:
#         if sorted(list(i[0])) == sorted(list(word)) and i.count(word) < strs.count(word):
#             i.append(word)
#             break
#     flag = True
#     for i in output:
#         if word in i:
#             flag = False
#             break
#     if flag:
#         output.append([word])
# print(output)

# Верное решение (Код с сайта)
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        temp_dict = defaultdict(list)

        for word in strs:
            sorted_str = ''.join(sorted(word))
            temp_dict[sorted_str].append(word)

        for group in temp_dict.values():
            output.append(group)

        return output