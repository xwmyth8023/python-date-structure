"""
栈操作如下：
1. Stack() 创建一个空的新栈。 它不需要参数，并返回一个空栈。
2. push(item)将一个新项添加到栈的顶部。它需要 item 做参数并不返回任何内容。
3. pop() 从栈中删除顶部项。它不需要参数并返回 item 。栈被修改。
4. peek() 从栈返回顶部项，但不会删除它。不需要参数。 不修改栈。
5. isEmpty() 测试栈是否为空。不需要参数，并返回布尔值。
6. size() 返回栈中的 item 数量。不需要参数，并返回一个整数。
"""

class Stack():
    def __init__(self,items):
        self.items = []
    
    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
