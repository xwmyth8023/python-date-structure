"""插入排序"""

def insert_sort(num_list):
    for i in range(1,len(num_list)):
        """
        假设有一个项已被排序，记为sorted_value,其索引记为sorted_index
        """
        sorted_value = num_list[i]
        sorted_index = i
        """
        如果该项的前一项比该项大，则将该项前移，直到没有前一项大于该项为止
        """
        while sorted_index > 0 and num_list[sorted_index-1] > sorted_value:
            
            num_list[sorted_index] = num_list[sorted_index-1] # 将该项的值修改为前一项的值
            sorted_index = sorted_index - 1
        
        num_list[sorted_index] = sorted_value # 将前一项的值修改为该项未被修改前的值


num_list = [54,26,93,17,77,31,44,55,20]
insert_sort(num_list)
print(num_list)
