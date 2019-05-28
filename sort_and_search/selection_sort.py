"""选择排序"""

def selection_sort(num_list):
    for i in range(len(num_list)-1,0,-1): #[8,7,6,5,4,3,2,1,0]
        max_index = 0 # 假设最大数的索引为0
        """
        在除最大值的list中查找是否存在大于假设的最大数的数字，如果存在，
        将最大值索引修改为该数字的索引j，直到list中没有更大的数，循环结束
        """
        for j in range(1,i+1): 
            if num_list[j] > num_list[max_index]:
                max_index = j
        """
        将num_list中最后一项的值修改为前面所得的最大数
        """
        temp = num_list[i]
        num_list[i] = num_list[max_index]
        num_list[max_index] = temp


num_list = [54,26,93,17,77,31,44,55,20]
selection_sort(num_list)
print(num_list)