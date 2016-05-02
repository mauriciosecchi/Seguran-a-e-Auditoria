import Util
import random


symbolsFile = "./tableSubs.txt"

def start(fileName):
    option = Util.menuSubstituicao()
    if option == 1:
        cript(fileName)
    elif option == 2:
        decript(fileName)
    elif option == 3:
        buildTable()


def cript(fileName):
    deSimbolos = readDeSimbolos()
    paraSimbolos = readParaSimbolos()
    inputFile = Util.scanFile(fileName)

    outputText = ""
    for item in inputFile:
        idx = deSimbolos.find(item)
        outputText += paraSimbolos[idx]

    #print(outputText)
    #Util.writeFile("./saidaCriptSubs.txt", outputText)
    return outputText

def decript(fileName):
    deSimbolos = readParaSimbolos()
    paraSimbolos = readDeSimbolos()
    fileName = "saidaCriptSubs.txt"
    inputFile = Util.scanFile(fileName)

    outputText = ""
    for item in inputFile:
        idx = deSimbolos.find(item)
        outputText += paraSimbolos[idx]

    print(outputText)
    Util.writeFile("./saidaTrabalho5.txt", outputText)


def buildTable():
    deSimbolos   = [chr(i) for i in xrange(0, 256)]
    aux          = [chr(i) for i in xrange(0, 256)]

    paraSimbolos = [chr(i) for i in xrange(0, 256)]

    symbols1 = ""
    symbols2 = ""

    for i in range(0, 256):
        idx = random.randint(0, len(aux)-1)
        paraSimbolos[i] = aux[idx]
        aux[idx] = aux[-1]
        del(aux[-1])
        symbols1 += deSimbolos[i]
        symbols2 += paraSimbolos[i]

    symbols1 + symbols2
    Util.writeFile(symbolsFile, symbols1+symbols2)

def readDeSimbolos():
    symbols = Util.scanFile(symbolsFile)

    deSimbolos = ""
    for i in range(0, 256):
        deSimbolos += symbols[i]

    return deSimbolos

def readParaSimbolos():
    symbols = Util.scanFile(symbolsFile)

    paraSimbolos = ""

    for i in range(256, len(symbols)):
        paraSimbolos += symbols[i]

    return paraSimbolos

def decriptT5(inputFile):
    deSimbolos = readParaSimbolos()
    paraSimbolos = readDeSimbolos()

    outputText = ""
    for item in inputFile:
        idx = deSimbolos.find(item)
        outputText += paraSimbolos[idx]

    return outputText

