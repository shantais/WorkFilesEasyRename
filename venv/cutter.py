def cutNames(file_list):
    cutLettersFromFileNames = list(file[-7:-4] for file in file_list)

    for idx, singularName in enumerate(cutLettersFromFileNames):
        if '-' in singularName:
            cutLettersFromFileNames[idx] = singularName.split('-')[1]
            
    return cutLettersFromFileNames