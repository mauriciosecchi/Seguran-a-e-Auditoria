import socket, string, random
import collections

input=[]
key=[]

#Função de criptografia Cifra de Cesar
def cifraCesar(key, input):
    tmp=0
    vec=[]
    for i in input:
        tmp = int(ord(i))
        tmp1 = int(ord(key[0]))
        res = (tmp + tmp1) % 256
        var = unichr(res).encode('Latin-1')
        vec.append(var)
    return vec

#Funçao para descriptografar a Cifra de Cesar
def decifraCesar(key, vec):
    tmp=0
    vec1=[]
    for i in vec:
        tmp = int(ord(i))
        tmp1 = int(ord(key[0]))
        res = (tmp - tmp1) % 256
        var = unichr(res).encode('Latin-1')
        vec1.append(var)
    return vec1

#Função de criptografia usando Cifra de Transposição
def cifraTranspose(key, input):
    mtx=[]
    lin=[]
    res=[]
    auxKey = int(key[0])
    if auxKey > len(input):
        print 'Erro: tamanho da matriz maior que a maior palavra'
        return res
    cont=0
    # monta a matriz
    for i in input:
        if cont < auxKey:
            lin.append(i)
        else:
            mtx.append(lin)
            auxKey = auxKey + int(key[0])
            lin = []
            lin.append(i)
        cont = cont + 1
    if cont <= auxKey:
        while cont < auxKey:
            lin.append(' ')
            cont = cont + 1
        mtx.append(lin)
    #Faz a matriz transposta
    mtxT = zip(*mtx)
    for i in mtxT:
        for j in i:
            res.append(j)
    return res 

#Função para descriptografar a cifra de Transposição
def decifraTranspose(key, cT):
    col=[]
    mtx=[]
    res=[]
    tmp = len(cT) / int(key[0])
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
            res.append(j)
    return res

#Função de cripitografia usando Cifra de Vigenere
def cifraVigenere(key, input):
    result=[]
    i = 0;
    j = 0;
    while True:
        if i == len(key):
            i = 0
        if j == len(input):
            break
        result.append(cifraCesar(key[i], input[j]))
        i = i + 1
        j = j + 1
    return result
       
#Função de descriptografia de Cifra de Vigenere
def decifraVigenere(key, cV):
    result=[]
    i = 0;
    j = 0;
    while True:
        if i == len(key):
            i = 0
        if j == len(cV):
            break
        result.append(decifraCesar(key[i], cV[j]))
        i = i + 1
        j = j + 1
    return result

#Função para montar a tabela para a cifra de Substituição
def montaTabela():
    result=[]
    tmp = set(range(0,256))
    tmp1 = bytearray(tmp)    
    i = 0;
    while len(tmp) > 0:
        r = random.choice(list(tmp))
        tmp1 = [i,r]
        result.append(bytearray(tmp1))
        tmp.remove(r)
        i += 1
    return result

#Função de criptografia com Cifra de Substituição
def cifraSubstituicao(table, input):
    result=[]
    #faz a substituicao
    for i in input:
        for j in table:
            tmp = int(ord(i))
            tmp1 = j.decode('Latin-1')
            aux = int(ord(tmp1[0]))
            if tmp == aux:
                result.append(unichr(int(ord(tmp1[1]))).encode('Latin-1'))
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

#Função para exibir o texto
def display(text):
    #Abertura de arquivo
    nameFile = 'saida.txt'
    fOut = open(nameFile, 'a')
    #Imprime texto
    for i in text:
        fOut.writelines(i)
    fOut.writelines('\n')
    fOut.close()

#funcao para leitura de arquivo
def readFile():
    nameFile = raw_input('Nome do arquivo: ')
    #abre o arquivo
    try:
        f = open(nameFile, 'r')
    except:
        print 'Erro: Fail open this file'
    #sai do laco quanto termina de ler todo o arquivo
    while True:
        buffer1 = ''
        #le a linha
        buffer1 = f.readline()
        #se acabou o arquivo para
        if not buffer1: break
        #le o texto da entrada
        for i in buffer1:
            #cria uma lista dos carecteres lidos da entrada
            input.append(i)
    f.close()

#Inicia a execução do programa
while True:
    print '1. Cifra Cesar'
    print '2. Cifra de Transposicao'
    print '3. Cifra de Vigenere'
    print '4. Cifra de Substituicao'
    print '5. Sair'

    opcao = raw_input('Opcao: ')

    if opcao == '1':
        cC=[]
        dC=[]
        key=[]
        input=[]
        key = raw_input('Informe um caracter para a chave: ')
        #le o arquivo
        readFile()
        #imprime o que o usuario informou
        #display(input)
        #Chama a função de criptografia Cifra Cesar
        cC = cifraCesar(key, input)
        #imprime a saida criptografado
        display(cC)
        #descriptografa usando a decifra Cesar
        dC = decifraCesar(key, cC)
        #imprime a saida descriptografado
        display(dC)
    elif opcao == '2':
        cT=[]
        dT=[]
        key=[]
        input=[]
        key = raw_input('Informe o numero para a chave: ')
        #le o arquivo
        readFile()
        #imprime o que o usuario informou
        #display(input)
        #Chama a função de criptografia Cifra de Transposição
        cT = cifraTranspose(key, input)
        #imprime a saida criptografado
        display(cT)
        #descriptografa
        dT = decifraTranspose(key, cT)
        #imprime a saida descriptografado
        display(dT)
    elif opcao == '3':
        cV=[]
        dV=[]
        key=[]
        input=[]
        key = raw_input('Informe a palavra chave: ')
        #le o arquivo
        readFile()
        #imprime o que o usuario informou
        #display(input)
        #Chama a função de criptografia Cifra de Vegenere
        cV = cifraVigenere(key, input)
        #imprime a saida criptografado
        display(cV)
        #descriptografa
        dV = decifraVigenere(key, cV)
        #imprime a saida descriptografado
        display(dV)
    elif opcao == '4':
        cS=[]
        dS=[]
        key=[]
        input=[]
        #le o arquivo
        readFile()
        #imprime o que o usuario informou
        #display(input)
        #monta a tabela
        tab = montaTabela()
        #Chama a função de criptografia Cigra de Substituição
        cS = cifraSubstituicao(tab, input)
        #imprime a cifra
        display(cS)
        #faz a descriptografia
        dS = decifraSubstituicao(tab, cS)
        #imprime a descriptografia
        display(dS)
    elif opcao == '5':
        break