#Arquivo com as funções de cifragem

#Funcao de criptografia Cifra de Cesar
def cifraCesar(key, input):
    tmp=0
    vec=[]
    tmp1 = int(key)
    for i in input:
        res = (i + tmp1) % 256
        vec.append(res)
    return vec

#Função de criptografia usando Cifra de Transposição
def cifraTranspose(key, input, fileCript):
    mtx=[]
    lin=[]
    res=""
    auxKey = int(key)
    if auxKey > len(input):
        print ('Erro: tamanho da matriz maior que a maior palavra')
        return res
    cont=0
    # monta a matriz
    for i in input:
          
        if cont < auxKey:
            lin.append(i)
        else:
            mtx.append(lin)
            auxKey = auxKey + int(key)
            lin = []
            lin.append(i)
        cont = cont + 1
    if cont < auxKey:
        while cont < auxKey:
            lin.append(' ')
            cont = cont + 1
        mtx.append(lin)
    #print mtx
    #Faz a matriz transposta
    mtxT = zip(*mtx)
    #print mtxT
    
    #texta se as duas entradas sao iguais "fincionalidade para não ataque"
    if input == fileCript:
        for i in mtxT:
            for j in i:
                res += j
    else:       #funcinalidade no ataque a cifra
        cont = 0 
        for i in mtxT:
            for j in i:
                if j == ' ' and fileCript[cont] == '\x00':  #teste é necessario pois quando é armazenado o espaço em branco ela é um valor null
                    j = fileCript[cont]
                elif j != fileCript[cont]:
                    return res
                res += j
                cont += 1 
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
       