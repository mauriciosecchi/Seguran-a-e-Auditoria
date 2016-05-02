import Util
import Cesar
import Vigenere
import Transposicao
import Substituicao
import QuebrarCifras
import AtaqueDicionario

fileName = "./entrada.txt"

option = Util.menuAlgoritmo()

while option != 0:
    if option == 1:
        Cesar.start(fileName)
    elif option == 2:
        Transposicao.start(fileName)
    elif option == 3:
        Vigenere.start(fileName)
    elif option == 4:
        Substituicao.start(fileName)
    elif option == 5:
        nomeArquivo = Util.scan("Arquivo: ")
        QuebrarCifras.quebrarCifra(nomeArquivo)
    elif option == 6:
        nomeArquivo = Util.scan("Arquivo: ")
        AtaqueDicionario.startAttack(nomeArquivo)

    option = Util.menuAlgoritmo()
