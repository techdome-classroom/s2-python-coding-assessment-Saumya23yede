# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         pass

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack to keep track of opening brackets
        stack = []
        
        # Dictionary to match closing brackets with opening brackets
        bracket_map = {')': '(', ']': '[', '}': '{'}
        
        # Traverse the input string
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack

solution = Solution()
print(solution.isValid("()"))         
print(solution.isValid("()[]{}"))    
print(solution.isValid("(]"))         
print(solution.isValid("([)]"))       
print(solution.isValid("{[]}"))       





    



  

