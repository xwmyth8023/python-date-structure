"""希尔排序"""

def shell_sort(num_list):
    n = len(num_list)
    step = n // 2
    """
    比较第index项和与第index项相隔step的项，如果第index项小于相隔step项，则交换位置
    """
    while step >= 1:
        for i in range(step, n):
            index = i
            while index - step >= 0:
                if num_list[index] < num_list[index - step]:
                    num_list[index], num_list[index-step] = num_list[index-step], num_list[index]
                    index -= step
                else:
                    break

        step //= 2

num_list = [54,26,93,17,77,31,44,55,20]
shell_sort(num_list)
print(num_list)