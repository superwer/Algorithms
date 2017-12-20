def bisect_search1(L,e):
    '''
    O(n log n) comlexity each recursive call copies the portion of the
    list
    '''
    if L==[]:
        return False
    elif len(L)==1:
        return L[0]==e
    else:
        half=len(L)//2
        if L[half]>e:
            return bisect_search1(L[:half],e)
        else:
            return bisect_search1(L[half:],e)