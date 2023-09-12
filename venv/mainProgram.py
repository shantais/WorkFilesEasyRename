import os
import cutter
import sorter
import namer

def main():
    directory = 'C:\\Users\\shant\\OneDrive\\Pulpit\\EM2023_2'
    name_base = 'em21'

    fileNameList = os.listdir(directory)
    cutfileNameList = cutter.cutNames(fileNameList)
    sortedNameList = sorter.sortNames(cutfileNameList)

    new_names = namer.rename(name_base, sortedNameList)

    i = 0
    while i < len(new_names):
        os.rename(directory + '\\' + fileNameList[i], directory + '\\' + new_names[i])
        i += 1

if __name__ == '__main__':
    main()