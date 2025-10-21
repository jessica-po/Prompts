class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if expression == 'f':
            return False
        if expression == 't':
            return True
        if expression[0] == '!':
            return not self.parseBoolExpr(expression[2:-1])
        if expression[0] == '|':
            cursor = 2
            while cursor < len(expression)-1:
                end_of_next = self.getNextExpr(expression, cursor)
                if self.parseBoolExpr(expression[cursor:end_of_next]):
                    return True
                cursor = end_of_next + 1
            return False
        if expression[0] == '&':
            cursor = 2
            while cursor < len(expression)-1:
                end_of_next = self.getNextExpr(expression, cursor)
                if not self.parseBoolExpr(expression[cursor:end_of_next]):
                    return False
                cursor = end_of_next + 1
            return True
    
    def getNextExpr(self, expression, start):
        if expression[start] == '!' or expression[start] == '|' or expression[start] == '&':
            open_count = 1
            close_count = 0
            start += 1
            while open_count > close_count:
                start += 1
                if expression[start] == '(':
                    open_count += 1
                if expression[start] == ')':
                    close_count += 1
                
            return start + 1
        else:
            return start + 1