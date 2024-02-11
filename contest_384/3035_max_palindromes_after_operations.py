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

words = ["abbb","ba","aa"]
charCount = [0]*26
for word in words:
    for char in word:
        charCount[ord(char)-ord('a')] += 1
print(charCount)
pairs = 0 
for count in charCount:
    pairs += int(count/2)
print(pairs)
words.sort(key=len)
total = 0
for word in words:
    pairsNeeded = int(len(word)/2)
    if pairs >= pairsNeeded:
        pairs -= pairsNeeded
        total += 1
print(total)