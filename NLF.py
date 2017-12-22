import random
import numpy as np

def inputTextFile(byLetter = False):
    output = []
    with open('steveSpeech.txt', 'r') as f:
        for line in f:
            output.extend(replacer(line).split(" "))
    if byLetter:
        return wordsToLetters(output)
    return output
        

def replacer(line):
    repList = ["[", "]", ":", "　", "\n", "", ".", ","]
    for rep in repList:
        line = line.replace(rep, "")
    return line

def wordsToLetters(words):
    letters = []
    for word in words:
        letters.extend(list(word))

    return letters

def countSame(targets):
    ranking = []
    for target in set(targets):
        ranking.append([target, targets.count(target)])
    return sorted(ranking, key=lambda ranking:ranking[:][1] , reverse=True)

def multipleWords(words, ml=2):
    mulWords = []
    if len(words) < ml:
        print("words length should be at least " + str(ml))
        return mulWords
    
    for idx,word in enumerate(words[0:len(words)-ml+1]):
        mulWord = word
        for i in range(ml-1):
            mulWord += " " + words[idx+i+1]
        mulWords.append(mulWord)
    return mulWords

def calcP(targets):
    wordSum = 0.
    for target in targets:
        wordSum += target[1]
    for idx, target in enumerate(targets):
        targets[idx][1] = target[1]/wordSum
    return targets

def generateRandomText(targets, length=100, byAddSpace=False):
    # format of targets
    # [["Apple",13], ["Vitamin", 5], ...]
    keyList = []
    output = []
    if byAddSpace:
        spacer = " "
    else:
        spacer = ""
    for idx, target in enumerate(targets):
        for i in range(target[1]):
            keyList.append(idx)
    keyLength = len(keyList)
    for i in range(length):
        rnd = random.randint(0,keyLength-1)
        output.append(targets[keyList[rnd]][0])
    return spacer.join(output)

def calcEntropy(targets):
    output = 0.
    targetsP = calcP(targets)
    for target in targetsP:
        output += target[1]*np.log(target[1])
    return output * -1
