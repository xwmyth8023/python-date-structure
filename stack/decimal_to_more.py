"""
计算机科学中，通常会使用很多不同的编码。其中最常见的是二级制，八进制和十六进制。
十进制233和它对应的八进制和十六进制 351(8),E9(16)
"""

from pythonds.basic.stack import Stack

def decimal_to_binary(decimal_num,base):
    """
    @decimal_num: inter 十进制数
    @base:inter 进制数
    """

    stack = Stack()
    remainders = '0123456789ABCDEF' # 最大进制数为16，所以是到F,为大于9的余数设置十六进制对应的字符
    result = ''

    """
    不断对n进行除进制数取余，并将余数加入栈
    """
    while decimal_num > 0:
        remainder = decimal_num % base
        stack.push(remainder)
        decimal_num = decimal_num // base
    """
    栈不为空的情况下，拼接所得的余数，返回最终对应的进制数字
    """
    while not stack.isEmpty():
        result = result + remainders[stack.pop()]

    return result

print(decimal_to_binary(233,2))
print(decimal_to_binary(233,8))
print(decimal_to_binary(31,16))