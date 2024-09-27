# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         pass

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store Roman numerals and their corresponding integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize total to 0
        total = 0
        # Traverse through the string
        for i in range(len(s)):
            # If this is not the last character and the current value is less than the next value, subtract it
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                # Otherwise, add the current value to total
                total += roman_map[s[i]]
        
        return total

# Test cases
solution = Solution()
print(solution.romanToInt("III"))       # Output: 3
print(solution.romanToInt("LVIII"))     # Output: 58
print(solution.romanToInt("MCMXCIV"))   # Output: 1994


