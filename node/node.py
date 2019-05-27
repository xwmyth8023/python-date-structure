"""
无序列表的结构是项的集合，其中每个项保持相对于其他项的相对位置。下面给出了一些可能的无序列表操作。
1. List() 创建一个新的空列表。它不需要参数，并返回一个空列表。
2. add(item) 向列表中添加一个新项。它需要 item 作为参数，并不返回任何内容。假定该 item 不在列表中。
3. remove(item) 从列表中删除该项。它需要 item 作为参数并修改列表。假设项存在于列表中。
4. search(item) 搜索列表中的项目。它需要 item 作为参数，并返回一个布尔值。
5. isEmpty() 检查列表是否为空。它不需要参数，并返回布尔值。
6. size（）返回列表中的项数。它不需要参数，并返回一个整数。
7. append(item) 将一个新项添加到列表的末尾，使其成为集合中的最后一项。它需要 item 作为参数，并不返回任何内容。假定该项不在列表中。
8. index(item) 返回项在列表中的位置。它需要 item 作为参数并返回索引。假定该项在列表中。
9. insert(pos，item) 在位置 pos 处向列表中添加一个新项。它需要 item 作为参数并不返回任何内容。假设该项不在列表中，并且有足够的现有项使其有 pos 的位置。
10. pop() 删除并返回列表中的最后一个项。假设该列表至少有一个项。
11. pop(pos) 删除并返回位置 pos 处的项。它需要 pos 作为参数并返回项。假定该项在列表中。
"""

class Node():
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnsortedList():

    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())