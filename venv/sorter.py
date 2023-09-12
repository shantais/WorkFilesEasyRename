def sortNames(cutFileNameList):
    for idx, name in enumerate(cutFileNameList):
        n1 = int(cutFileNameList[idx])
        index = idx+1
        while index < len(cutFileNameList):
            n2 = int(cutFileNameList[index])
            if n1 > n2:
                cutFileNameList[idx], cutFileNameList[index] = cutFileNameList[index], cutFileNameList[idx]
                n1 = int(cutFileNameList[idx])
            index += 1
            
    return cutFileNameList