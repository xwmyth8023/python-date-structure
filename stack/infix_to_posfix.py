from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
    """
    @infixexpr 表达式，如: A * B, 每个字符之间必须空格
    """
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
            print('1======', postfixList)
        elif token == '(':
            opStack.push(token)
            print('2=======',opStack.isEmpty())
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
                print('3======',postfixList)
        else: #当token = *时，
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                print('4=======',opStack.isEmpty())
                postfixList.append(opStack.pop())     
            opStack.push(token) # 将*加入栈中
            print('5======', postfixList)
            print('6=======',opStack.isEmpty())
    print('7======', postfixList)
    print('8=======',opStack.isEmpty())
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    print('9======', postfixList)
    return " ".join(postfixList)

print(infixToPostfix("A * B + C"))