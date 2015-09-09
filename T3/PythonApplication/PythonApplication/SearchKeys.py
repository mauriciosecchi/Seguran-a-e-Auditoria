#Arquivo com as funções que encontram a chave com o texto em claro
import DecriptFunctions
import Util

#Funçao para encontrar a chave
def cesar(fileCript, fileDecript):
    tmp = fileCript[0]
    tmp1 = fileDecript[0]
    #faz o calculo para identificar a chave
    key = (tmp - tmp1) % 256
    
    #decifra todo o arquivo
    dC = DecriptFunctions.decifraCesar(key, fileCript)
    if dC == fileDecript:
        print ('A chave esta correta!')
        print ('Key: ' + str(key))
    else:
        print ('A chave esta incorreta!')

#Funçao para encontrar a chave cifra de Vigenere
def vigenere(fileCript, fileDecript):
    cont=0
    i = 0;
    j = 0;
    var = ''
    while True:
        #faz o calculo para identificar a chave
        key = (fileCript[i] - fileDecript[i]) % 256
        var += chr(key)    
        i += 1
        dV = DecriptFunctions.decifraVigenere(var, fileCript, fileDecript)
        #texta se o texto decifrado e igual ao original
        if dV == fileDecript:
            print ('Key: ' + var)
            print ('A chave esta correta!')
            break

#Ataque a cifra de Transposição com o original e o aberto
def transpose(fileCript, fileDecript):
    result=[]
    key = 2
    while True:
        result = DecriptFunctions.decifraTranspose(key, fileCript)    #aplica a cifra no arquivo orifinal
        if key > len(fileDecript):
            break
        if result == fileDecript:     #testa se o resultado da crifa com a chave é igual ao arquivo original
            print ('A chave esta correta!')
            print ('Key: ' + key)
            break
        print (key)
        key += 1

#Funcao de ataque a cifra de substituição com arquivos em claro
def substitution(fileCript, fileDecript):
    table=[]
    tmp = set(range(0,256))
    tmp1 = bytearray(tmp)
    i = 0
    
    while True:
        j = 0
        while len(tmp) > 0:
            if unichr(j).encode('Latin-1') == fileDecript[i]:
                flag = 0
                #testa se o arquivo já existe na tabela, caso não insere na tabela
                for k in table:
                    temp = k.decode('Latin-1')
                    aux = ord(temp[0])
                    if j == aux:
                        flag = 1
                if flag == 0:
                    tmp1 = [j, fileCript[i]]
                    table.append(bytearray(tmp1))
                    print (j)
                    tmp.remove(j)
                    j = 0
                    break
            j += 1
            if j > len(tmp):
                break
        i += 1
        if len(fileDecript) == i:           #sai quando chegou ao final da entrada
            break
        if len(table) == 256:       #ou quando a tabela esta completa
            break
    # pega a tabela gerada e roda o algoritmo para decifrar       
    result = DecriptFunctions.decifraSubstituicao(table, fileCript)
    print ('Tabela:')
    for i in table:
        tmp1 = i.decode('Latin-1')
        print (tmp1)
    Util.display(result)