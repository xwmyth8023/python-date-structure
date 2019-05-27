"""
一个一世纪著名历史学家弗拉维奥·约瑟夫斯的传奇故事。
故事讲的是，他和他的 39 个战友被罗马军队包围在洞中。
他们决定宁愿死，也不成为罗马人的奴隶。他们围成一个圈，
其中一人被指定为第一个人，顺时针报数到第七人，就将他杀死。
约瑟夫斯是一个成功的数学家，他立即想出了应该坐到哪才能成为最后一人。
最后，他加入了罗马的一方，而不是杀了自己。
"""
from pythonds.basic.queue import Queue

def try_to_live(live_list, num):
    queue = Queue()

    for people in live_list:
        queue.enqueue(people)

    while queue.size() > 1:
        for i in range(num):
            print(i)
            queue.enqueue(queue.dequeue())
        queue.dequeue()

    return queue.dequeue()

print(try_to_live(['a','b','c','d','e','f'],7))