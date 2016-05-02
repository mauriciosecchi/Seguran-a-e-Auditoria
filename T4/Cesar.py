import Util

def start(fileName):
    option = Util.menuOperacao()
    if option == 1:
        key = int(Util.scan("Key: "))
        cript(fileName, key)
    elif option == 2:
        decript(fileName)

def cript(fileName, key):

    inputFile = Util.scanFile(fileName)
    outputText = ""

    for i in range(0, len(inputFile)):
        asciiCode = (ord(inputFile[i]) + key) % 256
        outputText = outputText + unichr(asciiCode).encode('Latin-1')#chr(asciiCode)

    return outputText

def criptCompare(inputFile, outputfile, key):
    idx = 0
    for i in range(0, len(inputFile)):
        asciiCode = (ord(inputFile[i]) + key) % 256
        if outputfile[idx] != chr(asciiCode):
            return False
        idx += 1
    return True

def decript2(inputFile, key):
    outputText = ""

    for i in range(0, len(inputFile)):
        asciiCode = (ord(inputFile[i]) - key) % 256
        outputText = outputText + unichr(asciiCode).encode('Latin-1')#chr(asciiCode)

    return outputText

def decript(fileName):
    key = int(Util.scan("Key: "))
    fileName = "saidaCriptCesar.txt"
    inputFile = Util.scanFile(fileName)
    outputText = ""

    for i in range(0, len(inputFile)):
        asciiCode = (ord(inputFile[i]) - key) % 256
        outputText = outputText + unichr(asciiCode).encode('Latin-1')#chr(asciiCode)

    print(outputText)
    Util.writeFile("./saidaDecriptCesar.txt", outputText)