"""
队列是项的有序结合，其中添加新项的一端称为队尾，移除项的一端称为队首,
当一个元素从队尾进入队列时，一直向队首移动，直到它成为下一个需要移除的元素为止.
队列操作如下:
1. Queue() 创建一个空的新队列。 它不需要参数，并返回一个空队列。
2. enqueue(item) 将新项添加到队尾。 它需要 item 作为参数，并不返回任何内容。
3. dequeue() 从队首移除项。它不需要参数并返回 item。 队列被修改。
4. isEmpty() 查看队列是否为空。它不需要参数，并返回布尔值。
5. size() 返回队列中的项数。它不需要参数，并返回一个整数。
"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)