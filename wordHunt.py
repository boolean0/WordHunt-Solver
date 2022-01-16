import time

moveHorz = [-1, -1, 0, 1, 1, 1, -1, 0]
moveVert = [0, -1, 1, -1, 0, 1, 1, -1]
grid = [['A', 'K', 'J', 'D'], ['B', 'U', 'Q', 'K'], ['S', 'A', 'R', 'E'], ['W', 'A', 'F', 'Y']]
wordList = []
foundWords = []
foundWordPaths = []

def processWordPath(wordLength, wordPath):
    finalPath = []
    for i in range(wordLength):
        finalPath.append(wordPath[i])
    
    return finalPath

def valid(x, y, xShift, yShift):
    return  x+xShift>=0 and x+xShift<4 and y+yShift>=0 and y+yShift<4

def direction(xShift, yShift):
    directionVector = ""
    if xShift > 0: directionVector += "D"
    elif xShift < 0: directionVector += "U"

    if yShift > 0: directionVector += "R"
    elif yShift < 0: directionVector += "L"

    return directionVector

def searchWord(x, y, wordIdx, wordLength, word, wordPath):

    if wordIdx == wordLength:
        return True

    if grid[x][y] == word[wordIdx]: 
        temp = grid[x][y]
        tempPath = wordPath
        grid[x][y] = '#'
        inGrid = False
        for i in range(8):
            wordPath = tempPath
            if valid(x, y, moveHorz[i], moveVert[i]):
                directionVector = direction(moveHorz[i], moveVert[i])
                wordPath.append(directionVector)
                inGrid = inGrid or searchWord(x+moveHorz[i], y+moveVert[i], wordIdx+1, wordLength, word, wordPath)
                

        grid[x][y] = temp
        wordPath.pop()
        return inGrid

    else: 
        wordPath.pop()
        return False

                

def main(): 
    with open('sortedwords.txt', 'r') as reader:
        for line in reader: 
            wordList.append(line.strip())

    #read input lol 
    
    for word in wordList:
        found = False
        for i in range(4):
            if found: break

            for j in range(4):
                if found: break

                else:    
                    startingSquare = (i ,j)
                    wordPath = []
                    wordPath.append(startingSquare)

                    if word[0] == grid[i][j] and searchWord(i, j, 0, len(word), word, wordPath): 
                            foundWords.append(word)
                            finalPath = processWordPath(len(word), wordPath)
                            foundWordPaths.append(finalPath)
                            found = True


            
    print(len(foundWords) , "words found:")

    for i in range(len(foundWords)):
        if i >= len(foundWordPaths): print(foundWords[i])
        else: print(foundWords[i] , ":",  foundWordPaths[i])


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
    