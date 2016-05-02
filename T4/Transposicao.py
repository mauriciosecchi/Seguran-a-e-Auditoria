import Util


def start(fileName):
    option = Util.menuOperacao()
    if option == 1:
        key = int(Util.scan("Key: "))
        cript(fileName, key)
    elif option == 2:
        decript(fileName)

def cript(fileName, key):
    inputFile  = Util.scanFile(fileName)
    outputText = ""

    matrix = []
    lines  = []

    idx = 0
    for item in inputFile:
        if idx < key:
            lines.append(item)
        else:
            matrix.append(lines)
            idx = 0
            lines = []
            lines.append(item)
        idx +=1

    while idx < key:
        lines.append('\0')
        idx += 1
    matrix.append(lines)
    transp = zip(*matrix)
    for i in transp:
        for j in i:
            outputText += j
    #print(outputText)
    #Util.writeFile("./saidaCriptTransp.txt", outputText)
    return outputText

def decript(fileName):
    key        = int(Util.scan("Key: "))
    fileName = "saidaCriptTransp.txt"
    inputFile  = Util.scanFile(fileName)
    outputText = ""

    matrix = []
    columns  = []
    lines = len(inputFile) / key

    idx = 0
    for item in inputFile:
        if idx < lines:
            columns.append(item)
        else:
            matrix.append(columns)
            idx = 0
            columns = []
            columns.append(item)
        idx +=1

    matrix.append(columns)
    transp = zip(*matrix)
    for i in transp:
        for j in i:
            outputText += j
    print(outputText)
    Util.writeFile("./saidaCriptTransp.txt", outputText)

def decript2(inputFile, key):
    outputText = ""

    matrix = []
    columns  = []
    lines = len(inputFile) / key

    idx = 0
    for item in inputFile:
        if idx < lines:
            columns.append(item)
        else:
            matrix.append(columns)
            idx = 0
            columns = []
            columns.append(item)
        idx +=1

    matrix.append(columns)
    transp = zip(*matrix)
    for i in transp:
        for j in i:
            outputText += j
    return outputText