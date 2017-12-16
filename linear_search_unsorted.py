def linear_search_usorted(L, e):
    '''
    O(len(L) comlexity
    must look through all elements to decide it's not there
    '''
    found = False
    for i in range (len(L)):
        if e == L[i]:
            found = True
    return found