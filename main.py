import NLF as it

if __name__=='__main__':
    # count letters
    print("---------------")
    letters = it.inputTextFile(byLetter = True)
    ranking = it.countSame(letters)
    print(ranking[0:5])
    
    # count words
    print("---------------")
    words = it.inputTextFile()
    ranking = it.countSame(words)
    print(ranking[0:5])
    
    # count 2 mul words
    print("---------------")
    words = it.inputTextFile()
    mlWords = it.multipleWords(words)
    ranking2 = it.countSame(mlWords)
    print(ranking2[0:5])
    
    # count 3 mul words
    print("---------------")
    words = it.inputTextFile()
    mlWords = it.multipleWords(words, ml=3)
    ranking3 = it.countSame(mlWords)
    print(ranking3[0:5])
    
    # generate text from letter
    print("---------------")
    letters = it.inputTextFile(byLetter = True)
    ranking = it.countSame(letters)
    generatedText = it.generateRandomText(ranking)
    print(generatedText)
    
    # generate text from 2 words
    print("---------------")
    generatedText = it.generateRandomText(ranking2, byAddSpace=True)
    print(generatedText)
    
    # generate text from 3 words
    print("---------------")
    generatedText = it.generateRandomText(ranking3, byAddSpace=True)
    print(generatedText)
    
    # calc entropy
    words = it.inputTextFile()
    letters = it.inputTextFile(byLetter = True)
    mlWords = it.multipleWords(words, ml=10)
    rankingL = it.countSame(letters)
    rankingW = it.countSame(words)
    ranking2 = it.countSame(mlWords)
    print(str(it.calcEntropy(rankingL)))
    print(str(it.calcEntropy(rankingW)))
    print(str(it.calcEntropy(ranking2)))

    
