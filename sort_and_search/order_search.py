"""顺序查找"""

def order_search(num_list,target):
    index = 0 
    found = False
    """从索引0开始查找，依次加1，直到找到目标"""
    while index < len(num_list) and not found:
        if num_list[index] != target:
            index += 1
        else:
            found = True
    return found

print(order_search([1,2,3,4,5,6],7))