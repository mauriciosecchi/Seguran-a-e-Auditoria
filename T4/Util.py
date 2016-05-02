from collections import Counter
from __builtin__ import dict


def scan(message):
   input = raw_input(message)
   return input


def scanFile(path):
    file = open(path, 'r')
    string = file.read()
    file.close()
    return string

def writeFile(path, message):
    file = open(path, "w")
    file.write(message)
    file.close()

def menuAlgoritmo():
    option = scan("\nEscolha o algoritmo de criptografia"
                  "\n1 - Cesar"
                  "\n2 - Transposicao"
                  "\n3 - Vigenere"
                  "\n4 - Substituicao"
                  "\n5 - Quebrar Cifra"
                  "\n6 - Ataque Dicionario"
                  "\n0 - Sair\n")
    return int(option)

def menuOperacao():
    option = scan("\n1 - Criptografar"
                  "\n2 - Descriptografar\n")
    return int(option)

def menuSubstituicao():
    option = scan("\n1 - Criptografar"
                  "\n2 - Descriptografar"
                  "\n3 - Gerar tabela\n")
    return int(option)

from string import punctuation


def unique_words(sentence):
    return set(sentence.translate(None, punctuation).lower().split())


def get_string_combination_letters(string, size):
    result = []
    m = []
    while size > 0:
        limit = len(string) - size + 1
        for i in range(0, limit):
            result.append(string[i:i+size])
        size -= 1
        for i in result:
            m.append(i)
    return result


def get_string_combination_letters3(string, size):
    result = []
    m = []
    while size > 0:
        limit = len(string) - size + 1
        for i in range(0, limit):
            result.append(string[i:i+size])
        size -= 1
        z = Counter(result)
        for i in range(0, len(z)):
            m.append(z[i])
    return m


def get_string_combination_letters2(string, size):
    result = []
    limit = len(string) - size + 1
    for i in range(0, limit):
        result.append(string[i:i+size])
    return result


def get_count_list(_list):
    return Counter(_list)


def get_compared_lists(_list1, _list2):
    _list1 = sorted(zip(_list1.itervalues(), _list1.iterkeys()), reverse=True)
    _list2 = sorted(zip(_list2.itervalues(), _list2.iterkeys()), reverse=True)
    _ret = []
    for a, b in zip(_list1, _list2):
        _ret.append((a[1], b[1]))
    return _ret


def get_word_pattern(word):
    output = ""
    actual = 1
    for i in range(0, len(word)):
        idx = word.index(word[i])
        if idx >= i:
            idx = -1
        if idx == -1:
            output += str(actual)
            actual += 1
        else:
            output += output[idx]
    return output


def get_text_words_pattern(text):
    l1 = get_count_list(get_string_combination_letters(text, 1))
    l2 = [[]]
    for word in text.split(l1.most_common()[0][0]):
        l2.append((word, get_word_pattern(word)))
    return l2


def get_unique_words_and_patterns(k):
    padroes_utilizados = ""
    list_remocao = []
    palavras = [[]]
    for i in range(1, len(k)):
        if k[i][1] + " " not in padroes_utilizados:
            palavras.append((k[i][0], k[i][1]))
            padroes_utilizados += " " + k[i][1]
        else:
            list_remocao.append(k[i][1] + " ")

    final = [[]]
    final = palavras
    '''for item in list_remocao:
        for i in range(1, len(palavras)):
            #print(item + " " + palavras[i][1])
            if item.strip() != palavras[i][1].strip():
                final.append(palavras[i])'''

    return final


def get_most_common_char(string):
    return Counter(string).most_common()[0][0]
str2 = scanFile("./books/livros.txt")

'''print "1"
dicionario = get_text_words_pattern(str2[0:4000])
print "2"
dicionario1 = get_unique_words_and_patterns(dicionario)
print "3"

#print(dicionario)
escape = get_most_common_char("jzphfp5yw5ee5a5ii")
texto_escuro = get_unique_words_and_patterns(get_text_words_pattern("jzphfp5yw5ee5a5ii".replace(escape, " ")))


saida = []

for i in range(1, len(texto_escuro)):
    for j in range(1, len(dicionario)):
        if dicionario[i][1] == texto_escuro[j][1]:
            saida.append(dicionario[i][0])

print(dicionario)
print texto_escuro
'''