"""
回文是一个字符串，读取首尾相同的字符，例如，radar toot madam。
"""

from pythonds.basic.deque import Deque

def palindrome_check(palindrome_string):

    deque = Deque()
    isEqual = True

    for ch in palindrome_string:
        deque.addRear(ch)
    
    while deque.size()>1 and isEqual:
        """取首尾字符进行比较"""
        begin = deque.removeFront()
        end = deque.removeRear()
        if begin != end:
            isEqual = False
        
    return isEqual

print(palindrome_check('aba'))
print(palindrome_check('abad'))