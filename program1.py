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
            # If it's a closing bracket
            if char in bracket_map:
                # Pop from stack if it's not empty, else use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped bracket matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)
        
        return not stack

# Test cases
solution = Solution()
print(solution.isValid("()"))         
print(solution.isValid("()[]{}"))    
print(solution.isValid("(]"))         
print(solution.isValid("([)]"))       
print(solution.isValid("{[]}"))       





    



  

