import socket, string, random
import collections

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
    tmp1 = int(ord(key[0]))
    for i in vec:
        tmp = int(ord(i))  
        res = (tmp - tmp1) % 256
        var = unichr(res).encode('Latin-1')
        vec1.append(var)
    return vec1

#Funçao para encontrar a chave
def searchKeyCesar(fileCript, fileDecript):
    tmp = ord(fileCript[0])
    tmp1 = ord(fileDecript[0])
    #faz o calculo para identificar a chave
    key = (tmp - tmp1) % 256
    
    var = unichr(key).encode('Latin-1')
    #decifra todo o arquivo
    dC = decifraCesar(var, fileCript)
    if dC == fileDecript:
        print 'A chave esta correta!'
        print 'Key: ' + str(key)
        display(['Cesar: ', str(key)])
    else:
        print 'A chave esta incorreta!'

#Funçao para encontrar a chave cifra de Vigenere
def searchKeyVigenere(fileCript, fileDecript):
    cont=0
    result=[]
    i = 0;
    j = 0;
    while True:
        tmp = ord(fileCript[i])
        tmp1 = ord(fileDecript[i])
        #faz o calculo para identificar a chave
        key = (tmp - tmp1) % 256
        var = unichr(key).encode('Latin-1')
        result.append(var)
        i += 1

        dV = decifraVigenere(result, fileCript, fileDecript)
        #texta se o texto decifrado e igual ao original
        if dV == fileDecript:
            print 'Key: '
            print result
            print 'A chave esta correta!'
            display(['Vigenere: ', result])
            break


#Função de criptografia usando Cifra de Transposição
def cifraTranspose(key, input, fileCript):
    mtx=[]
    lin=[]
    res=[]
    auxKey = int(key)
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
                res.append(j)
    else:       #funcinalidade no ataque a cifra
        cont = 0 
        for i in mtxT:
            for j in i:
                if j == ' ' and fileCript[cont] == '\x00':  #teste é necessario pois quando é armazenado o espaço em branco ela é um valor null
                    j = fileCript[cont]
                elif j != fileCript[cont]:
                    return res
                res.append(j)
                cont += 1 
    return res 

#Ataque a cifra de Transposição com o original e o aberto
def searchKeyTranspose(fileCript, fileDecript):
    result=[]
    key = 2
    while True:
        result = cifraTranspose(key, fileDecript, fileCript)    #aplica a cifra no arquivo orifinal
        if key > len(fileDecript):
            break
        if result == fileCript:     #testa se o resultado da crifa com a chave é igual ao arquivo original
            print 'A chave esta correta!'
            print 'Key: '
            print key
            break
        print key
        key += 1


#Função para descriptografar a cifra de Transposição
def decifraTranspose(key, cT):
    col=[]
    mtx=[]
    res=[]
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
def decifraVigenere(key, cV, fileDecript):
    i = 0
    j = 0
    result=[]
    while True:
        tmp=[]
        if i == len(key):
            i = 0
        if j == len(cV):
            break
        tmp1 = ord(key[i])
        tmp = ord(cV[j])  
        res = (tmp - tmp1) % 256
        var = unichr(res).encode('Latin-1')
        result.append(var)
        if fileDecript[j] != result[j]:
            break
        i = i + 1
        j = j + 1
    return result

#Funcao de ataque a cifra de substituição com arquivos em claro
def searchTableSubstitution(fileCript, fileDecript):
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
                    print j
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
    result = decifraSubstituicao(table, fileCript)
    print 'Tabela:'
    for i in table:
        tmp1 = i.decode('Latin-1')
        print tmp1
    display(result)


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
    fOut = open(nameFile, 'wb')
    #Imprime texto
    for i in text:
        fOut.writelines(i)
    #fOut.writelines('\n')
    fOut.close()

#funcao para leitura de arquivo
def readFile(nameFile):
    
    input=[]
    #abre o arquivo
    try:
        f = open(nameFile, 'rb')
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
    return input

#Inicia a execução do programa
while True:
    print '1. Cifra Cesar'
    print '2. Cifra de Transposicao'
    print '3. Cifra de Vigenere'
    print '4. Cifra de Substituicao'
    print '5. Sair'

    opcao = raw_input('Opcao: ')

    if opcao == '1':
        print '1. Cifra'
        print '2. Decifra'
        print '3. Ataque com arquivo em claro'
        op = raw_input('Opcao: ')

        if op == '1':
            #le o arquivo
            input = readFile("entrada.txt")
            key = raw_input('Informe um caracter para a chave: ')            
            #Chama a função de criptografia Cifra Cesar
            cC = cifraCesar(key, input)
            #imprime a saida criptografado
            display(cC)
        elif op == '2':
            #le o arquivo
            input = readFile("saida.txt")
            key = raw_input('Informe um caracter para a chave: ')            
            #Chama a função de criptografia Cifra Cesar
            dC = decifraCesar(key, input)
            #imprime a saida criptografado
            display(dC)
        elif op == '3':
            #le o arquivo
            fileCript = readFile('arquivos/outputs/pg11.txt.enc')
            fileDecript = readFile('arquivos/inputs/pg11.txt')
            #ataque a texto usando a cifra de Cesar com texto em claro
            searchKeyCesar(fileCript, fileDecript)

    elif opcao == '2':
        print '1. Cifra'
        print '2. Decifra'
        print '3. Ataque com arquivo em claro'
        op = raw_input('Opcao: ')
        
        if op == '1':
            key = raw_input('Informe o numero para a chave: ')
            #le o arquivo
            input = readFile('entrada.txt')
            #Chama a função de criptografia Cifra de Transposição
            cT = cifraTranspose(key, input, input)
            #imprime a saida criptografado
            display(cT)
        elif op == '2':
            key = raw_input('Informe o numero para a chave: ')
            #le o arquivo
            input = readFile('saida.txt')
            #Chama a função de criptografia Cifra de Transposição
            dT = decifraTranspose(key, input)
            #imprime a saida criptografado
            display(dT)
        elif op == '3':      
            #le o arquivo
            fileCript = readFile('arquivos/outputs/pg1342.txt.enc')
            fileDecript = readFile('arquivos/inputs/pg1342.txt')
            #fileCript = readFile('saida.txt')
            #fileDecript = readFile('entrada.txt')
            #ataque a texto usando a cifra de Vigenere com texto em claro
            searchKeyTranspose(fileCript, fileDecript)
    elif opcao == '3':
        print '1. Cifra'
        print '2. Decifra'
        print '3. Ataque com arquivo em claro'
        op = raw_input('Opcao: ')
        
        if op == '1':
            #le o arquivo
            input = readFile("entrada.txt")
            key = raw_input('Informe a palavra chave: ')           
             #Chama a função de criptografia Cifra de Vegenere
            cV = cifraVigenere(key, input)
            #imprime a saida criptografado
            display(cV)
        elif op == '2':
            input = readFile("saida.txt")
            key = raw_input('Informe a palavra chave: ')           
             #Chama a função de criptografia Cifra de Vegenere
            dV = decifraVigenere(key, input)
            #imprime a saida criptografado
            display(dV)
        elif op == '3':
            #le o arquivo
            fileCript = readFile('arquivos/outputs/pg174.txt.enc')
            fileDecript = readFile('arquivos/inputs/pg174.txt')
            #ataque a texto usando a cifra de Vigenere com texto em claro
            searchKeyVigenere(fileCript, fileDecript)

    elif opcao == '4':
        print '1. Cifra'
        print '2. Decifra'
        print '3. Ataque com arquivo em claro'
        op = raw_input('Opcao: ')
        
        #monta a tabela
        tab = montaTabela()

        #for i in tab:
        #    x = i.decode('Latin-1')
        #   print unichr(ord(x[0])).encode('Latin-1'), unichr(ord(x[1])).encode('Latin-1')        

        if op == '1':
             #le o arquivo
            input = readFile("entrada.txt")
            #Chama a função de criptografia Cigra de Substituição
            cS = cifraSubstituicao(tab, input)
            #imprime a cifra
            display(cS)
        elif op == '2':
            #faz a descriptografia
            dS = decifraSubstituicao(tab, cS)
            #imprime a descriptografia
            display(dS)
        elif op == '3':
            #le o arquivo
            fileCript = readFile("saida1.txt")
            fileDecript = readFile("entrada.txt")
            #fileCript = readFile('arquivos/outputs/pg74.txt.enc')
            #fileDecript = readFile('arquivos/inputs/pg74.txt')

            #Ataque a função com arquivo em claro
            searchTableSubstitution(fileCript, fileDecript)      
        
        
    elif opcao == '5':
        break