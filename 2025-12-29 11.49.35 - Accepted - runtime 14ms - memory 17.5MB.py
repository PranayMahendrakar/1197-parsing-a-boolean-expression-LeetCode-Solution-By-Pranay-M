class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for char in expression:
            if char == ',' or char == '(':
                continue
            elif char == 't':
                stack.append(True)
            elif char == 'f':
                stack.append(False)
            elif char in '!&|':
                stack.append(char)
            elif char == ')':
                # Collect all boolean values until we hit the operator
                values = []
                while stack and stack[-1] not in ['!', '&', '|']:
                    values.append(stack.pop())
                if stack:
                    op = stack.pop()
                    if op == '!':
                        stack.append(not values[0])
                    elif op == '&':
                        stack.append(all(values))
                    else:  # op == '|'
                        stack.append(any(values))
        
        return stack[0]