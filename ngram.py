import random

def nSplit(n):
    s = open('log.txt', 'r').read()
    length = len(s)
    splittedList = []
    tempString = ''
    index = n
    biIndex = 0

    for letter in s:
        if letter != '\n':
            if letter == '`':
                if len(tempString) > 0:
                    if tempString[len(tempString) - 1] == '`':
                        splittedList.append(tempString)
                        tempString = '`'
                    else:
                        tempString += '`'
                else:
                    tempString += '`'
            elif letter == ' ' and biIndex != index:
                tempString += ' '
                splittedList.append(tempString)
                tempString = ''
                biIndex = 0
            elif letter ==' ' and biIndex == index:
                tempString += ' '
                splittedList.append(tempString)
                tempString = ''
                biIndex = 0
            elif biIndex == index:
                splittedList.append(tempString)
                tempString = letter
                biIndex = 1
            else:
                tempString += letter
                biIndex += 1
        else:
            biIndex = 0
            #tempString = ''
            continue
    splittedList.append(tempString)
    #print splittedList
    return splittedList

def addToDict(splitWords):
    dict = {}
    index = 0
    while index < len(splitWords) - 1:
        if index + 1 > len(splitWords) - 1:
            break
        elif splitWords[index] not in dict:
            dict[splitWords[index]] = [splitWords[index + 1]]
        else:
            dict[splitWords[index]].append(splitWords[index + 1])
        index += 1
    #print dict
    return dict

def join(dict):
    starterWords = []
    currentWord = ''
    combinedString = ''

    for word in dict.keys():
        if word[0] == '`':
            starterWords.append(word)
    currentWord = random.sample(starterWords, 1)[0]
    
    while True:
        if currentWord[len(currentWord) - 1] == '`':
            combinedString += currentWord
            break
        else:
            combinedString += currentWord
            currentWord = random.sample(dict[currentWord], 1)[0]
    #print combinedString
    return combinedString[1:-1]


def run(n = 3):
    x = nSplit(n)
    return join(addToDict(x))

print(run(4))