if __name__ == '__main__':
    listOfNum = []
    nestList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        listOfNum.append(score)
        nestList.append([name, score])
    listOfNum.sort()
    minScore = -1
    for score in listOfNum:
        if score != listOfNum[0]:
            minScore = score
            break
    listOfNames = []
    for arr in nestList:
        if arr[1] == minScore:
            listOfNames.append(arr[0])
    listOfNames.sort()
    for name in listOfNames:
        print(name)
    


