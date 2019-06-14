class Reverse:
    def __init__(self,x):
        self.val = x
        self.next = None

def reverse(head):
    if head is None or head.next is None:
        return head
    #假设1-->2-->3-->4-->5-->None
    previous = None
    current = head #1
    newhead = head #1
    while current:
        newhead = current
        if newhead is not None:
            print('newhead===',newhead.val)
        tmp = current.next
        if tmp is not None: 
            print('tmp===',tmp.val)
        current.next = previous#none 
        if current.next is not None and previous is not None:
            print('current.next',current.next.val,'previous',previous.val)
        previous = current
        if previous is not None:
            print('previous===',previous.val)
        current = tmp 
        if current is not None:
            print('current===',current.val)
    return newhead

head=Reverse(1)  #测试代码
p1=Reverse(2)   #建立链表1->2->3->4->None;
p2=Reverse(3)
p3=Reverse(4)
head.next=p1
p1.next=p2
p2.next=p3
p=reverse(head)  #输出链表 4->3->2->1->None