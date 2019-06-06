"""
符号字符串如
{ { ( [ ] [ ] ) } ( ) }
[ [ { { ( ( ) ) } } ] ]
[ ] [ ] [ ] ( ) { }
这些被恰当的匹配了，因为不仅每个开始符号都有对应的结束符号，而且符号的类型也匹配。
相反这些字符串没法匹配：
( [ ) ]
( ( ( ) ] ) )
[ { ( ) ]
"""

from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":  #如果符号在‘([{’里，加入栈
            s.push(symbol)
        else: # symbol in ")]}"
            if s.isEmpty(): #如果栈为空，则不匹配，返回false
                balanced = False
            else: # 如果栈不为空
                top = s.pop() # 弹出顶部项
                if not matches(top,symbol): # 比较顶部项与当前的symbol，如果不匹配，返回false
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    """
    opens.index('(') = 0 
    closers.index(')') = 0
    '(' 和 ')'刚好匹配，返回true 
    """
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close) 


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))