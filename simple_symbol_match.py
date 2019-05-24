"""
括号匹配意味着每个开始符号具有相应的结束符号，并且括号能被正确嵌套。考虑下面正确匹配的括号字符串：
(()()()())
(((())))
(()((())()))
对比那些不匹配的括号：
((((((())
()))
(()()(()
"""

from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('()()()'))
print(parChecker(')('))