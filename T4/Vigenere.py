import Util
import itertools
import math

def start(fileName):
    option = Util.menuOperacao()
    if option == 1:
        key = Util.scan("Key: ")
        inputFile = Util.scanFile(fileName)
        cript(inputFile, key)
    elif option == 2:
        decript(fileName)


def buildKey(key, length):
    output = key
    while (len(output) < length):
        output = output + key
    return output


def cript(inputFile, key):
    #fileName = "entrada.txt"
    #inputFile = Util.scanFile(fileName)
    #key = buildKey(key, len(inputFile))
    lenKey = len(key)
    outputText =  ""

    i = 0
    for item in inputFile:
        if i == lenKey:
            i = 0

        asciiCode = (ord(item) + ord(key[i])) % 256
        i += 1
        outputText = outputText + chr(asciiCode)
        #.encode('Latin-1')#chr(asciiCode)

    #print(outputText)
    #Util.writeFile("./saidaCriptVigenere.txt", outputText)
    return outputText


#Se retornar -1, e porque e impossivel gerar com essa subchave.
#Se retornar 0, entao esta errado mas a proxima chave pode dar certo
#Se retornar 2, entao a chave esta correta
def criptStatusReturn(inputFile, outputFile, key):
    lenKey = len(key)
    ret = -1
    i = 0
    idx = 0
    for item in inputFile:
        if i == lenKey:
            i = 0
            ret = 0
        asciiCode = (ord(item) + ord(key[i])) % 256
        if chr(asciiCode) != outputFile[idx]:
            if i == 0:
                ret = -1
            return ret
        i += 1
        idx += 1
    ret = 1
    return ret

def decript(fileName):
    key = Util.scan("Key: ")
    fileName = "./saidaCriptVigenere.txt"
    inputFile = Util.scanFile(fileName)
    key = buildKey(key, len(inputFile))

    outputText = ""
    i = 0
    for item in inputFile:
        #print(list(item))
        if i == len(key):
            i = 0

        asciiCode = ord(item) - ord(key[i])
        asciiCode = asciiCode % 256
        outputText = outputText + unichr(asciiCode).encode('Latin-1')#chr(asciiCode)

        i += 1
        #print(item)
    #for i in range(0, len(inputFile)-1):
    #    asciiCode = ord(inputFile[i]) - ord(key[i])

    #    asciiCode = abs(asciiCode % 256)
    #    #if asciiCode < 0:
    #     #   asciiCode = asciiCode + 256

     #   outputText = outputText + chr(asciiCode)

    print(outputText)
    Util.writeFile("./saidaDecriptVigenere.txt", outputText)


def decript2(inputFile, key):
    lenKey = len(key)
    i = 0
    idx = 0
    outputText = ""
    for item in inputFile:
        if i == lenKey:
            i = 0
        asciiCode = (ord(item) - ord(key[i])) % 256
        outputText = outputText + unichr(asciiCode).encode('Latin-1')#chr(asciiCode)
        i += 1
        idx += 1
    return outputText

def decript3(inputFile, key):
    output = []
    #key = key * ((len(inputFile)/len(key)) +1)
    key = itertools.cycle(key)
    #for i in range(1, len(inputFile)):
    for (a,b) in zip(key, inputFile):
        asciiCode = (ord(b) - ord(a)) % 256
        output.append(chr(asciiCode))
    return ''.join(output)