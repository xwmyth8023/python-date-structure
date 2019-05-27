"""
假设你想将一个整数转换为一个二进制和十六进制字符串。
例如，将整数 10 转换为十进制字符串表示为 10，或将其字符串表示为二进制 1010。
"""

def to_str(n,base):
    """
    @n: int
    @base: int 2,8,10,16
    """

    remains = '0123456789ABCDE' # 2到16进制余数表示

    if n < base:
        return remains[n]
    else:
        # remain = remains[n%base]
        # n = n//base
        return to_str(n//base,base) + remains[n%base]

"""利用栈实现"""

from pythonds.basic.stack import Stack

stack = Stack()
def to_str_with_stack(n,base):
    result = ''
    remains = '0123456789ABCDE'

    while n > 0:
        if n < base:
            stack.push(remains[n])
        else:
            stack.push(remains[n%base])
        n = n//base
    
    while not stack.isEmpty():
        result = result + stack.pop()
    return result

print(to_str(1453,16))
print(to_str_with_stack(1453,16))