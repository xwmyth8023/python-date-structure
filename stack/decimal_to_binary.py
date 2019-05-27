"""
我们如何能够容易地将整数值转换为二进制呢？答案是“除 2”算法，它用栈来跟踪二进制结果的数字。
“除 2” 算法假定我们从大于 0 的整数开始。不断迭代的将十进制除以 2，并跟踪余数。第一个除以 
2 的余数说明了这个值是偶数还是奇数。偶数有 0 的余数，记为 0。奇数有余数 1，记为 1.我们将
得到的二进制构建为数字序列，第一个余数实际上是序列中的最后一个数字。
""" 

from pythonds.basic.stack import Stack

def decimal_to_binary(decimal_num):
    stack = Stack()
    result = ''

    """
    不断对n进行除2取余数，并讲余数加入栈
    """
    while decimal_num > 0:
        remainder = decimal_num % 2
        stack.push(remainder)
        decimal_num = decimal_num // 2
    """
    栈不为空的情况下，拼接所得的余数，返回最终所得的二进制数字
    """
    while not stack.isEmpty():
        result = result + str(stack.pop())

    
    return result

print(decimal_to_binary(233))