import Util
#Arquivo com as funções de cifragem

#Funçao para descriptografar a Cifra de Cesar
def decifraCesar(key, vec):
    tmp=0
    vec1=[]
    tmp1 = int(key)
    for i in vec: 
        res = (i - tmp1) % 256
        vec1.append(res)
    return vec1

#Função para descriptografar a cifra de Transposição
def decifraTranspose(key, cT):
    col=[]
    mtx=[]
    res=""
    tmp = len(cT) / key
    auxKey = tmp
    cont = 0
    for i in cT:
        if cont < auxKey:
            col.append(i)
        else:
            mtx.append(col)
            auxKey = auxKey + tmp
            col = []
            col.append(i)
        cont = cont + 1
    
    mtx.append(col)
    #Faz a matriz transposta
    mtxT = zip(*mtx)
    #Imprime a matriz normal
    for i in mtxT:
        for j in i:
            res += j
    return res

#Função de descriptografia de Cifra de Vigenere
def decifraVigenere(key, cV, fileDecript):
    i = 0
    j = 0
    result=[]
    while True:
        if i == len(key):
            i = 0
        if j == len(cV):
            break
        tmp1 = ord(key[i])
        res = (cV[j] - tmp1) % 256
        result.append(res)
        if fileDecript[j] != result[j]:
            break
        i = i + 1
        j = j + 1
    return result

#Função para descriptografar utilizando a Cifra de Substituição
def decifraSubstituicao(table, input):
    result=[]
    for i in input:
        for j in table:
            tmp = int(ord(i))
            tmp1 = j.decode('Latin-1')
            aux = int(ord(tmp1[1]))
            if tmp == aux:
                result.append(unichr(int(ord(tmp1[0]))).encode('Latin-1'))
    return result

#Funçao para descriptografar a Cifra de Cesar modificada
def modDecCesar(key, vec):
    tmp1 = int(key)
    outFile = ""
    for i in vec: 
        res = (i - tmp1) % 256
        outFile += chr(res)
    return outFile

#Função modificada decifra de Vigenere
def modDecVigenere(key, cV):
    i = 0
    j = 0
    result=[]
    while True:
        if i == len(key):
            i = 0
        if j == len(cV):
            break
        tmp1 = ord(key[i])
        res = (cV[j] - tmp1) % 256
        result.append(res)
        i = i + 1
        j = j + 1
    return result

#Função modificada para descriptografar a cifra de Transposição
def moDecTranspose(key, cFile):
    col=[]
    mtx=[]
    res=""
    tmp = len(cFile) / key
    auxKey = tmp
    cont = 0
    for i in cFile:
        if cont < auxKey:
            col.append(i)
        else:
            mtx.append(col)
            auxKey = auxKey + tmp
            col = []
            col.append(i)
        cont = cont + 1
    
    mtx.append(col)
    #Faz a matriz transposta
    mtxT = zip(*mtx)
    #Imprime a matriz normal
    for i in mtxT:
        for j in i:
            res += j
    return res

#Função de descriptografia de Cifra de Vigenere
def modDecVigenere(key, cV):
    i = 0
    j = 0
    result=""
    while True:
        if i == len(key):
            i = 0
        if j == len(cV):
            break
        tmp1 = ord(key[i])
        res = (cV[j] - tmp1) % 256
        result += chr(res)
        i = i + 1
        j = j + 1
    return result