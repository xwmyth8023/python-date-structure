def tower_of_hanoi(n,left,mid,right):
    if n >=1:
        tower_of_hanoi(n-1,left,right,mid)
        tower_of_hanoi(1,left,mid,right)
        tower_of_hanoi(n-1,mid,left,right)