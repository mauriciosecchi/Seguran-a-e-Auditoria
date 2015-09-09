import Util
import DecriptFunctions
import string
import itertools

#Ataque a arquivo em escuro com cifra de Cesar
def usedCesar(inputFile, dictionary):
    best = 0
    key = 0
    percent = 0

    setDictionary = Util.setWords(dictionary)
    for i in range(0, 256):
        tmp = DecriptFunctions.modDecCesar(i, inputFile)
        uniqueWords = Util.setWords(tmp)
        nWords = len(uniqueWords & setDictionary)
        print("Key: " + str(i) + " Total de palavras: " + str(nWords))
        if nWords > best:
            best = nWords
            key = i
            countWords = len(uniqueWords)
            percent = (best*100)/countWords
        if percent > 40:
            break
    
    print("\nAlgoritmo de Cesar"
                              "\nChave: " + str(key) +
                              "\nTotal de palavras: " + str(countWords) +
                              "\nTotal de palavras encontradas: " + str(best) +
                              "\n" + str(percent) + "% de acerto" ) 

#Ataque a arquivo em escuro com a cifra de Cesar
def usedVigenere(inputFile, dictionary):
    best = 0
    key = 0
    percent = 0

    #listChars = ['a','b','c','d']
    listChars = ['1','2','3','4','5','6']

    setDictionary = Util.setWords(dictionary)
    for sizeKey in range(1, len(listChars)+1):
       for i in itertools.product(listChars, repeat=sizeKey):
            print(i)
            tmp = DecriptFunctions.modDecVigenere(i, inputFile[0:240])
            uniqueWords = Util.setWords(tmp)
            nWords = len(uniqueWords & setDictionary)

            if nWords > best:
                best = nWords
                key = i
                countWords = len(uniqueWords)
                percent = (best*100)/countWords

            if percent > 50:
                break    
    print("\nAlgoritmo de Vigenere"
                              "\nChave: " + str(key) +
                              "\nTotal de palavras: " + str(countWords) +
                              "\nTotal de palavras encontradas: " + str(best) +
                              "\n" + str(percent) + "% de acerto" )
    
#Ataque sem arquivo em claro com a cifra de Transposição
def usedTranspose(inputFile, dictionary):
    best = 0
    key = 0
    percent = 0

    setDictionary = Util.setWords(dictionary)
    for i in range(2, 256):
        tmp = DecriptFunctions.moDecTranspose(i, inputFile)
        uniqueWords = Util.setWords(tmp)
        nWords = len(uniqueWords & setDictionary)
        print("Key: " + str(i) + " Total de palavras: " + str(nWords))
        if nWords > best:
            best = nWords
            key = i
            countWords = len(uniqueWords)
            percent = (best*100)/countWords
        if percent >= 50:
            break
    
    print("\nAlgoritmo de Transpose"
                              "\nChave: " + str(key) +
                              "\nTotal de palavras: " + str(countWords) +
                              "\nTotal de palavras encontradas: " + str(best) +
                              "\n" + str(percent) + "% de acerto" )