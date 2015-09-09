import socket, string, random
import collections
from string import punctuation
#File with the function of context general

def menuPrincipal():
    print ('1. Cifra Cesar')
    print ('2. Cifra de Transposicao')
    print ('3. Cifra de Vigenere')
    print ('4. Cifra de Substituicao')
    print ('5. Sair')
    opcao = input('Opcao: ')
    return opcao

def menuSec():
    print ('1. Cifra')
    print ('2. Decifra')
    print ('3. Ataque com arquivo em claro')
    print ('4. Ataque no escuro')
    op = input('Opcao: ')
    return op

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

#Função para exibir o texto
def display(text):
    #Imprime texto
    for i in text:
        var = chr(i)
        print (var)

def writeFile(path, message):
    file = open(path, "w")
    for i in message:
        var = i
        file.write(var)
    file.close()

#funcao para leitura de arquivo retornando valor ascii
def readFile(nameFile):
    
    inp=[]
    #abre o arquivo
    try:
        f = open(nameFile, 'rb')
    except:
        print ('Erro: Fail open this file')
    #sai do laco quanto termina de ler todo o arquivo
    
    buffer1 = ''
    #le a linha
    buffer1 = f.read()
    #le o texto da entrada
    for i in buffer1:
        #cria uma lista dos carecteres lidos da entrada
        inp.append(i)

    f.close()
    return inp

#Função de abertura de arquivo
def rFile(nameFile):
    f = open(nameFile, 'r')
    buffer = f.read()
    f.close()
    return buffer


#pega somente as palavras unicas armazenadas na variavel passado no parametro
def setWords(sentence):
    transtable = {ord(c): None for c in punctuation}
    sentence = set(sentence.translate(transtable).lower().split())
    return sentence


