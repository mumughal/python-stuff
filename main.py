
import re
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide (divident, divisor):
    return divident / divisor

def subtract(x, y):
    return x - y

def check_more_precedence(x, y):
    if (y in ['(', ')']) or (x in ['(', ')']) or (x in ['+', '-'] and y == ['*', '/']):
        return False
    else:
        return True

def solve(operator, x, y):
    if operator == '+':
        return add(x, y)
    elif operator == '-':
        return subtract(x, y)
    elif operator == '*':
        return multiply(x, y)
    else:
        return divide(x, y)

def calculate(equation):
    operators = ["*", "/", "(", ")", "+", "-"]
    operator_stack = []
    number_stack = []

    splitted_equation = re.split("([()+-/*])", equation)
    splitted_equation = [x.strip(' ') for x in splitted_equation]
    for x in splitted_equation:
        if x in operators:
            if operator_stack == []:
                operator_stack.append(x)
            elif check_more_precedence(x, operator_stack[len(operator_stack)-1]):
                less_precednece_op = operator_stack.pop()
                number2 = number_stack.pop()
                number1 = number_stack.pop()
                result = solve(less_precednece_op, number1, number2)
                number_stack.append(result)
                operator_stack.append(x)
            elif x == ')':
                y = ''
                while y != '(':
                    stack_top_operand = operator_stack.pop()
                    number2 = number_stack.pop()
                    number1 = number_stack.pop()
                    result = solve(stack_top_operand, number1, number2)
                    number_stack.append(result)
                    y = operator_stack[len(operator_stack)-1]
                    if operator_stack[len(operator_stack)-1] == '(':
                        operator_stack.pop()
            elif x:
                operator_stack.append(x)
                
        elif x:
            x = x.strip()
            number_stack.append(int(x))

    while operator_stack != []:
        stack_top_operand = operator_stack.pop()
        number2 = number_stack.pop()
        number1 = number_stack.pop()
        result = solve(stack_top_operand, number1, number2)
        number_stack.append(result)

    return number_stack.pop()

