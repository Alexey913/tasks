# Given two strings ransomNote and magazine, return true if
# ransomNote can be constructed by using the letters
# from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_list = [i for i in magazine]
        for ch in ransomNote:
            if ch in magazine_list:
                magazine_list.remove(ch)
            else:
                return False
        return True