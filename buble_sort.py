'''
    buble sort, compares consecutive pairs of elements, swap elements in
    pair such that smaller is first, when reaches end of the list, start over
    again, stop when no more swaps have been made.
    
    O(n^2) complexity
    '''
def buble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L [j]:
                swap = False
#                temp = L[j]
#                L[j] = L[j-1]
#                L[j-1] = temp
                L[i],L[i-1]=L[i-1],L[i]