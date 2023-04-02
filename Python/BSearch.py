def binary_search(alist, token):
    low = 0
    high = len(alist) - 1

    while (low <= high): 
        mid = (low + high) // 2 
        midvalue = alist[mid]

        #print("\n", "mid", mid, "midvalue", midvalue)

        if token == midvalue: 
            return mid

        if token < midvalue: 
            # slice away the upper part of the list
            high =  mid -1
            #alist = alist[:mid]
        else: 
            # slice away the lower part of the list 
            low = mid + 1
           # alist = alist[mid+1:]

    return -100

"""def binary_search(alist, token):

    while alist: 
        mid = len(alist) // 2 
        midvalue = alist[mid]

        #print("\n", "mid", mid, "midvalue", midvalue)

        if token == midvalue: 
            return True

        if token < midvalue: 
            # slice away the upper part of the list
            alist = alist[:mid]
        else: 
            # slice away the lower part of the list 
            alist = alist[mid+1:]

    return False"""
