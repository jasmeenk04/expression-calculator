#Author: Jasmeen Kaur
#calculator.py

#Input: The math expression you want solved
#Output: Your expression solved
from tree import ExpTree
from stack import Stack

def separate_decimals(string):
    digits = []
    decimal = False
    for char in string:
        if char.isdigit():
            digits.append(char)
        elif char == "." and not decimal:
            digits.append(char)
            decimal = True
        else:
            break
    return "".join(digits), len(digits)


def infix_to_postfix(infix):
    operatorvalue = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    operators = ["-", "+", "*", "/", "^", "(", ")"]
    operators = set(operators)
    opstack = Stack()
    ex = ""
    loser = None
    for index, s in enumerate(infix):
        if loser != None:
            if loser > index:
                continue
        if s.isdigit():
            value, cocomelons = separate_decimals(infix[index:])
            loser = cocomelons+index
            ex += value+" "
        elif s == "(":
            opstack.push("(")
        elif s == ")":
            while opstack.stack_items != [] and opstack.peek() != "(":
                ex += opstack.pop()+" "
            opstack.pop()
        else:
            while opstack.stack_items != [] and opstack.peek() != "(" and operatorvalue[s] <=operatorvalue[opstack.peek()]:
                ex += opstack.pop()+" "
            opstack.push(s)
    while opstack.stack_items != []:
        ex += opstack.pop()+" "
    return ex[:-1]

def calculate(infix):
    postfixvalue = infix_to_postfix(infix)
    evalvalue = ExpTree.make_tree(postfixvalue.split())
    solution = ExpTree.evaluate(evalvalue)
    return solution

# a driver to test calculate module
if __name__ == '__main__':
    
    print("Welcome to Calculator Program!")
    while True:
        key = input("Please enter your expression here. To quit enter 'quit' or 'q':\n")
        if key == "q" or key == "quit":
            print("Goodbye!")
            break
        else:
            print(calculate(key))



    

    # test infix_to_postfix function
    #assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    #assert infix_to_postfix('5+2*3') == '5 2 3 * +'
    # test calculate function
    #assert calculate('(5+2)*3') == 21.0
    #assert calculate('5+2*3') == 11.0
    
