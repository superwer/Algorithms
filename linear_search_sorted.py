def linear_search_sorted(L,e):
    '''
    must only look until reach a number greater than e
    O(len(L)) complexity
    '''
    
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False