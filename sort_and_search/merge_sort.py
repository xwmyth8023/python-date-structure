"""归并排序"""

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            print('1-',lefthalf,'----------',righthalf)
            if lefthalf[i] < righthalf[j]: 
                alist[k]=lefthalf[i] 
                print('2===',alist)
                i=i+1 
                print("3===",i)
            else: 
                alist[k]=righthalf[j] 
                print("4===",alist)
                j=j+1
                print("5===",j)
            k=k+1 
        print("6===========",k)

        while i < len(lefthalf): 
            print("7========",lefthalf)
            alist[k]=lefthalf[i]
            print("8========",alist)
            i=i+1 
            k=k+1 
            print("9====",i,k)

        while j < len(righthalf):
            print("10======",righthalf)
            alist[k]=righthalf[j]
            print("11==",alist)
            j=j+1 
            k=k+1 
            print("12===",j,k)
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)