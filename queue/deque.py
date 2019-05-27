"""
deque（也称为双端队列）是与队列类似的项的有序集合。
它有两个端部，首部和尾部，并且项在集合中保持不变。
deque 不同的地方是添加和删除项是非限制性的。
可以在前面或后面添加新项。同样，可以从任一端移除现有项。
在某种意义上，这种混合线性结构提供了单个数据结构中的栈和队列的所有能力。

deque 操作如下：
1. Deque() 创建一个空的新 deque。它不需要参数，并返回空的 deque。
2. addFront(item) 将一个新项添加到 deque 的首部。它需要 item 参数 并不返回任何内容。
3. addRear(item) 将一个新项添加到 deque 的尾部。它需要 item 参数并不返回任何内容。
4. removeFront() 从 deque 中删除首项。它不需要参数并返回 item。deque 被修改。
5. removeRear() 从 deque 中删除尾项。它不需要参数并返回 item。deque 被修改。
6. isEmpty() 测试 deque 是否为空。它不需要参数，并返回布尔值。
7. size() 返回 deque 中的项数。它不需要参数，并返回一个整数。
"""

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)