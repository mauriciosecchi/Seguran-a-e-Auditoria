import Util
import Cesar
import Transposicao
import Vigenere


def quebrarCifra(nomeArquivo):
    nomeEntrada = "./inputs/" + nomeArquivo
    nomeSaida = "./outputs/" + nomeArquivo +  ".enc"

    #quebrou = tryCesarCompare(nomeEntrada, nomeSaida)
    #if not quebrou:
     #   quebrou = trySubstituicao(nomeEntrada, nomeSaida)
    #if not quebrou:
        #quebrou = tryVigenere(nomeEntrada, nomeSaida)
    quebrou = tryTransposicao(nomeEntrada, nomeSaida)
    #if not quebrou:
     #   quebrou = tryTransposicao(nomeEntrada, nomeSaida)
    if not quebrou:
        print("Nao foi possivel quebrar a cifra")


def tryCesar(nomeEntrada, nomeSaida):
    inputFile = Util.scanFile(nomeEntrada)
    outputFile = Util.scanFile(nomeSaida)

    key = (ord(outputFile[0]) - ord(inputFile[0])) % 256
    retornoCesar = Cesar.cript(nomeEntrada, key)
    #if filecmp.cmp(nomeSaida, "./saidaCriptCesar.txt"):
    if retornoCesar == outputFile:
        print("Algoritmo: Cifra de Cesar\nChave: " + str(key))
        return True
    return False

def tryCesarCompare(nomeEntrada, nomeSaida):
    inputFile = Util.scanFile(nomeEntrada)
    outputFile = Util.scanFile(nomeSaida)

    key = (ord(outputFile[0]) - ord(inputFile[0])) % 256
    retornoCesar = Cesar.criptCompare(inputFile, outputFile, key)
    if retornoCesar:
        print("Algoritmo: Cifra de Cesar2\nChave: " + str(key))
        return True
    return False

def tryTransposicao(nomeEntrada, nomeSaida):
    inputFile = Util.scanFile(nomeEntrada)
    outputFile = Util.scanFile(nomeSaida)
    key = 1

    while(key < len(inputFile)):
        retornoTransposicao = Transposicao.cript(nomeEntrada, key)
        #if(filecmp.cmp(nomeSaida, "./saidaCriptTransp.txt")):
        if retornoTransposicao == outputFile:
            print("Algoritmo: Cifra de Transposicao\nChave: " + str(key))
            return True
        key += 1

    return False


def trySubstituicao(nomeEntrada, nomeSaida):
    paraSimbolos   = ['\0' for i in xrange(0, 256)]
    deSimbolos   = [chr(i) for i in xrange(0, 256)]

    inputFile = Util.scanFile(nomeEntrada)
    outputFile = Util.scanFile(nomeSaida)

    for i in range(0, len(inputFile)):
        idx = ord(inputFile[i])
        if(paraSimbolos[idx] != '\0' and paraSimbolos[idx] != outputFile[i]):
            return False
        paraSimbolos[idx] = outputFile[i]

    print("Algoritmo: Cifra de Substituicao\nChave: \n" + str(deSimbolos) +  "\n" + str(paraSimbolos))
    return True


def tryVigenere(nomeEntrada, nomeSaida):
    inputFile = Util.scanFile(nomeEntrada)
    outputFile = Util.scanFile(nomeSaida)
    lenInputFile = len(inputFile)
    key = ""
    idx = 0

    while(idx < lenInputFile):
        key += chr((ord(outputFile[idx]) - ord(inputFile[idx])) % 256)
        retornoVigenere = Vigenere.cript(inputFile, key)
        #if(filecmp.cmp(nomeSaida, "./saidaCriptVigenere.txt")):
        if retornoVigenere == outputFile:
            print("Algoritmo: Cifra de Vigenere\nChave: " + key)
            return True
        idx += 1

    return False

def tryVigenere2(nomeEntrada, nomeSaida):
    inputFile = Util.scanFile(nomeEntrada)
    outputFile = Util.scanFile(nomeSaida)
    lenInputFile = len(inputFile)
    key = ""
    idx = 0

    while(idx < lenInputFile):
        key += chr((ord(outputFile[idx]) - ord(inputFile[idx])) % 256)
        vigenereReturn = Vigenere.criptStatusReturn(inputFile, outputFile, key)
        if vigenereReturn == 1:
            print("Algoritmo: Cifra de Vigenere2\nChave: " + key)
            return True
        elif vigenereReturn == -1:
            return False
        idx += 1

    return False
