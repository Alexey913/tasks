# Given a roman numeral, convert it to an integer.

s = "MCMXCIV"
roman_dict = {
    'I': 1, 'V': 5, 'X': 10,
    'L': 50, 'C': 100,
    'D': 500, 'M': 1000
}
new_s = s[::-1]
res = roman_dict[new_s[0]]
for i in range(1, len(new_s)):
    if roman_dict[new_s[i]] < roman_dict[new_s[i-1]]:
        res -= roman_dict[new_s[i]]
    else:
        res += roman_dict[new_s[i]]
print(res)