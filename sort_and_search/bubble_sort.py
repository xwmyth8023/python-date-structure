"""
冒泡排序：最好的情况O(1)，最坏的情况O(n^2)
"""

def bubble_sort(num_list):
    """
    i = 8, j = 0, [26,54,93,17,77,31,44,55,20]
    i = 8, j = 1, [26,54,93,17,77,31,44,55,20]
    i = 8, j = 2, [26,54,17,93,77,31,44,55,20]
    ... 
    i = 8,找出最大的数置于末尾，再依次找出i = 7 时的最大数字，置于剩余数字末尾
    """
    for i in range(len(num_list)-1,0,-1): # [8,7,6,5,4,3,2,1,0]
        """
        从索引0开始，比较前后两个数字大小，如果前一个数字小于后一个数字，
        则交换位置；然后改为从索引1开始，依次类推
        """
        for j in range(0, i):
            if num_list[j] > num_list[j+1]:
                temp = num_list[j]
                num_list[j] = num_list[j+1]
                num_list[j+1] = temp
                

num_list = [54,26,93,17,77,31,44,55,20]
bubble_sort(num_list)
print(num_list)