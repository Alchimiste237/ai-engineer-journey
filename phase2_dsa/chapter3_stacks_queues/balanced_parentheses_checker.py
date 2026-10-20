from LIFO import Stack

def is_balanced(expression):
    """
    Check if brackets/parentheses are properly balanced.
    e.g. "({[]})" → True
         "({[})"  → False
         "(("     → False
    """
    stack = Stack()
    matching = {")": "(", "}": "{", "]": "["}
    opening = set("({[")

    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in matching:
            if stack.is_empty():
                return False           # closing bracket with nothing open
            if stack.pop() != matching[char]:
                return False           # mismatched pair
    return stack.is_empty()            # True only if nothing left open

# Tests
print(is_balanced("({[]})"))    # True
print(is_balanced("({[}])"))    # False — mismatched
print(is_balanced("(("))        # False — unclosed
print(is_balanced(""))
