def bub(bList):
    for i in range(len(bList)-1):
        if bList[i] > bList[i+1]:
            bList[i], bList[i+1] = bList[i+1], bList[i]
            bub(bList)
    return bList

