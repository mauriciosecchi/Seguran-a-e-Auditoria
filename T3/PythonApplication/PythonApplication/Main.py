import cProfile
import Util
import CriptFunctions
import DecriptFunctions
import SearchKeys
import Atach



#Inicia a execução do programa
while True:
    opcao = Util.menuPrincipal()

    if opcao == '1':
        op = Util.menuSec()

        if op == '1':
            #le o arquivo
            ent = Util.readFile("entrada.txt")
            key = input('Informe um caracter para a chave: ')            
            #Chama a função de criptografia Cifra Cesar
            cC = CriptFunctions.cifraCesar(key, ent)
            #imprime a saida criptografado
            Util.writeFile("saidaC.txt", cC)
            Util.display(cC)
        elif op == '2':
            #le o arquivo
            ent = Util.readFile("saidaC.txt")
            key = input('Informe um caracter para a chave: ')            
            #Chama a função de criptografia Cifra Cesar
            dC = DecriptFunctions.decifraCesar(key, ent)
            #imprime a saida criptografado
            Util.display(dC)
        elif op == '3':
            #le o arquivo
            fileCript = Util.readFile('arquivos/outputs/pg11.txt.enc')
            fileDecript = Util.readFile('arquivos/inputs/pg11.txt')
            #ataque a texto usando a cifra de Cesar com texto em claro
            SearchKeys.cesar(fileCript, fileDecript)
        elif op == '4':
            #le o arquivo cifrado
            fileInput = Util.readFile('arquivos/outputs/pg11.txt.enc')
            # le o arquivo do dicionario
            dictionary = Util.rFile('arquivos/inputs/pg1342.txt')
            # chama funcao para descoberta da chave
            cProfile.run('Atach.usedCesar(fileInput, dictionary)')
    elif opcao == '2':
        op = Util.menuSec()
        
        if op == '1':
            key = input('Informe o numero para a chave: ')
            #le o arquivo
            ent = Util.rFile('entrada.txt')
            #Chama a função de criptografia Cifra de Transposição
            #cProfile.run('cifraTranspose(key, ent)')
            cT = CriptFunctions.cifraTranspose(key, ent)
            #imprime a saida criptografado
            Util.writeFile('saida.txt', cT)
            #display(cT)
        elif op == '2':
            key = input('Informe o numero para a chave: ')
            #le o arquivo
            ent = Util.rFile('arquivos/outputs/pg1661.txt.enc')
            #Chama a função de criptografia Cifra de Transposição
            #cProfile.run('decifraTranspose(key, ent)')
            dT = DecriptFunctions.decifraTranspose(int(key), ent)
            #imprime a saida criptografado
            Util.writeFile("saida11.txt", dT)
        elif op == '3':      
            #le o arquivo
            fileCript = Util.rFile('arquivos/outputs/pg1342.txt.enc')
            fileDecript = Util.rFile('arquivos/inputs/pg1342.txt')
            #fileCript = readFile('saida.txt')
            #fileDecript = readFile('entrada.txt')
            #ataque a texto usando a cifra de Transposição com texto em claro
            SearchKeys.transpose(fileCript, fileDecript)
            #cProfile.run('searchKeyTranspose(fileCript, fileDecript)')
        elif op == '4':
            inputFile = Util.rFile('saida.txt')#
            dictionary = Util.rFile('arquivos/dictionary.txt')
            cProfile.run('Atach.usedTranspose(inputFile, dictionary)')
    elif opcao == '3':
        op = Util.menuSec()
        
        if op == '1':
            #le o arquivo
            ent = Util.readFile("entrada.txt")
            key = input('Informe a palavra chave: ')           
             #Chama a função de criptografia Cifra de Vegenere
            cV = CriptFunctions.cifraVigenere(key, ent)
            #imprime a saida criptografado
            Util.display(cV)
        elif op == '2':
            ent = Util.readFile("saida.txt")
            key = input('Informe a palavra chave: ')           
             #Chama a função de criptografia Cifra de Vegenere
            dV = DecriptFunctions.decifraVigenere(key, ent)
            #imprime a saida criptografado
            Util.display(dV)
        elif op == '3':
            #le o arquivo
            fileCript = Util.readFile('arquivos/outputs/pg174.txt.enc')
            fileDecript = Util.readFile('arquivos/inputs/pg174.txt')
            #ataque a texto usando a cifra de Vigenere com texto em claro
            print ('Abriu o arquivo')
            cProfile.run('SearchKeys.vigenere(fileCript, fileDecript)')
            #searchKeyVigenere(fileCript, fileDecript)
        elif op == '4':
            inputFile = Util.readFile('arquivos/outputs/pg27827.txt.enc')
            dictionary = Util.rFile('arquivos/dictionary.txt')
            cProfile.run('Atach.usedVigenere(inputFile, dictionary)')
    elif opcao == '4':
        op = Util.menuSec()     
        #monta a tabela
        tab = Util.montaTabela()

        #for i in tab:
        #    x = i.decode('Latin-1')
        #   print unichr(ord(x[0])).encode('Latin-1'), unichr(ord(x[1])).encode('Latin-1')        

        if op == '1':
             #le o arquivo
            ent = Util.readFile("entrada.txt")
            #Chama a função de criptografia Cigra de Substituição
            cS = CriptFunctions.cifraSubstituicao(tab, ent)
            #imprime a cifra
            Util.display(cS)
        elif op == '2':
            #faz a descriptografia
            dS = DecriptFunctions.decifraSubstituicao(tab, cS)
            #imprime a descriptografia
            Util.display(dS)
        elif op == '3':
            #le o arquivo
            fileCript = Util.readFile("saida1.txt")
            fileDecript = Util.readFile("entrada.txt")
            #fileCript = Util.readFile('arquivos/outputs/pg74.txt.enc')
            #fileDecript = Util.readFile('arquivos/inputs/pg74.txt')

            #Ataque a função com arquivo em claro
            SearchKeys.substitution(fileCript, fileDecript)      
             
    elif opcao == '5':
        break