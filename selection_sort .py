'''
selection sort, 
1-extract minimum element swap it with element at index 0
2-in remaining sublist, extract min element, swap it with the element at index 1
3-keep the left portion of the list sorted, at the i-th step, first i elements are
sorted, all other elemeents are bigger than first i elements

O(n^2) complexity
'''
def selection_sort(L):
    suffixSt=0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt],L[i] = L[i],L[suffixSt]
        suffixSt+=1

#L=[9,8,7,6,5,4,3,2,1,11,12,23,42,5,43]
#print(selection_sort(L))