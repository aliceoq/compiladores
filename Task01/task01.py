stack = []

def isOperation(op):
    if op == '*' or op == '+' or op == '-' or op == '/':
        return True
    else:
        return False

def execOperation(op):
    if len(stack) < 2:
        return

    n1 = stack.pop()
    n2 = stack.pop()
    result = 0

    if op == '*':
        result = n1 * n2
    elif op == '+':
        result = n1 + n2
    elif op == '-':
        result = n2 - n1
    elif op == '/':
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

f = open("Calc1.stk", "r")

# Assumindo que os elementos da entrada são separados por quebra de linha
# E os números podem ser decimais e negativos
for line in f:
    element = line.strip()
    if isOperation(element):
        execOperation(element)
    elif isNumber(element):
        stack.append(float(element))
    else:
        print('Invalid line: ' + line)
        break

if len(stack) == 1:
    print(stack.pop())