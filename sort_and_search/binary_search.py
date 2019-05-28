"""二分查找"""

def binary_search(num_list,target):
    small = 0
    big = len(num_list)-1
    found = False
    """每次从中间项开始查找，直到找到目标为止"""
    while small < big and not found:
        mid = (small+big)//2
        if num_list[mid] == target:
            found = True
        else:
            if num_list[mid] < target: #如果目标大于中间项，则把中间项设为small,big不变，继续在中间项和big之间查找
                small = mid + 1
            else: #如果目标小于中间项，则把中间项设为big,small不变，继续在small和中间项之间查找
                big = mid - 1
    return found

print(binary_search([1,12,30,4,8,56],13))