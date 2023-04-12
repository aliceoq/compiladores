from token_type import TokenType
from scanner import Scanner

s = Scanner()
stack = []
tokens = s.scan('input1.stk')

def isOperation(op):
    if op == TokenType.MINUS or op == TokenType.PLUS or op == TokenType.STAR or op == TokenType.SLASH:
        return True
    else:
        return False

def execOperation(op):
    if len(stack) < 2:
        return

    n1 = stack.pop()
    n2 = stack.pop()
    result = 0

    if op == TokenType.STAR:
        result = n1 * n2
    elif op == TokenType.PLUS:
        result = n1 + n2
    elif op == TokenType.MINUS:
        result = n2 - n1
    elif op == TokenType.SLASH:
        if n1 == 0:
            print('Invalid operation: division by zero')
            return
        result = n2 / n1

    stack.append(result)

def isNumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

for token in tokens:
    type = token.type
    value = token.lexeme
    print(token)
    if type == TokenType.NUM:
        stack.append(float(value))
    elif isOperation(type):
        execOperation(type)

if len(stack) == 1:
    print(stack.pop())