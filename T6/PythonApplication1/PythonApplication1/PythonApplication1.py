import random

def menuPrincipal():
    print ('1. Soma')
    print ('2. Multiplicacao')
    print ('3. Divisao')
    print ('4. Exponenciacao')
    print ('5. Subtracao')
    print ('6. Inverso Multiplicativo')
    print ('7. Algoritmo Ditfie Hellmann')
    print ('8. Sair')
    opcao = input('Opcao: ')
    return opcao

def menuOperando():
    op = input('Insira o operando: ')
    return op

#Soma
def sum(op1, op2):
    #concatena 0 para ficarem com o mesmo tamanho
    
    while len(op1) > len(op2):
        op2 = '0' + op2
    while len(op1) < len(op2):
        op1 = '0' + op1
    result = []
    i = 0
    #faz a soma dos números
    while True:
        if len(op1) == i or len(op2) == i:
            break
        else:
            result.append(int(op1[i]) + int(op2[i]))
        i += 1
    #calcula o carry
    return carryOver(result)

#Faz a propagacao do carry em uma lista
def carryOver(var):
    final = []
    quocient = 0
    var.reverse()    
    for i in var:
        i = i + quocient
        quocient = int(i / 10)
        rest = i % 10
        final.append(rest)
    if quocient > 0:
        final.append(quocient)
    final.reverse()
    return final

#Multiplicacao
def multiplication(op1, op2):
    final = []
    f = 0
    if op1[0] == '-':
        op1 = op1[1:len(op1)]
        f += 1
    if op2[0] == '-':
        op2 = op2[1:len(op2)]
        f += 1

    for i in op1:
        result = []
        for j in op2:
            result.append(int(i) * int(j))
        final.append(carryOver(result))
    #soma as listas
    sum_list = [0 for i in range(0, len(op1) + len(op2))]
    final.reverse()
    cont = 0
    for i in range(0, len(final)):
        final[i].reverse()
        for j in range(0, len(final[i])):
            sum_list[j+cont] = final[i][j] + sum_list[j+cont]
        cont += 1
    sum_list.reverse()
    result = carryOver(sum_list)
    while result[0] == 0: result.pop(0)
    #Descomentar se for necessário multiplicacao com numeros negativos
    if f == 1:
        result.insert(0,'-')
    return result

#Subtracao
def minus(op1, op2):
    
    result = ''

    while len(op1) > len(op2):
        op2 = '0' + op2
    while len(op1) < len(op2):
        op1 = '0' + op1
    
    test = 0
    if op1 > op2:
        num = [int(i) for i in op1]
        denum = [(~int(i) + 1) for i in op2]
    else:
        num = [int(i) for i in op2]
        denum = [(~int(i) + 1) for i in op1]
        test = 1
    carry = 0
    num.reverse()
    denum.reverse()
    vet = []

    for a,b in zip(num, denum):
        if carry == 1:
            a = a - 1
        if a + b >= 0:
            vet.append(a + b)
            carry = 0
        else:
            vet.append(10 + a + b)
            carry = 1
    vet.reverse()
    while vet[0] == 0 and len(vet) > 1: vet.pop(0)
    if test == 1:
         result = '-' + toString(vet)
    else:
        result = toString(vet)
    return result

#Subtracao versao para o inverso multiplicativa
def minus3(op1, op2):

    while len(op1) > len(op2):
        op2 = '0' + op2
    while len(op1) < len(op2):
        op1 = '0' + op1
    
    num = [int(i) for i in op1]
    denum = [(~int(i) + 1) for i in op2]

    carry = 0
    num.reverse()
    denum.reverse()
    vet = []

    for a,b in zip(num, denum):
        if carry == 1:
            a = a - 1
        if a + b >= 0:
            vet.append(a + b)
            carry = 0
        else:
            vet.append(10 + a + b)
            carry = 1
    vet.reverse()
    while vet[0] == 0 and len(vet) > 1: vet.pop(0)
    return vet

#Subtracao versao para a divisao
def minus2(op1, op2):
    
    while len(op1) > len(op2):
        op2.insert(0, 0) 
    while len(op1) < len(op2):
        op1.insert(0, 0)

    num = [int(i) for i in op1]
    denum = [(~int(i) + 1) for i in op2]
    carry = 0
    num.reverse()
    denum.reverse()
    vet = []

    for a,b in zip(num, denum):
        if carry == 1:
            a = a - 1
        if a + b >= 0:
            vet.append(a + b)
            carry = 0
        else:
            vet.append(10 + a + b)
            carry = 1
    vet.reverse()
    return vet

#Subtracao errado com comparação de bit
def minus1(op1, op2):
    num_bit =  bin(int(op1))
    aux = bin(int(op2))
    num_bit = num_bit[2:len(num_bit)]
    aux = aux[2:len(aux)]
    den_bit = ""

    #concatena 0 para ficarem com o mesmo tamanho
    if len(num_bit) > len(aux):
        aux = '0' + aux
    elif len(num_bit) < len(aux):
        num_bit = '0' + num_bit
    
    #faz a inversao
    for i in aux:
        if i == '1':
            den_bit += '0'
        else:
            den_bit += '1'
    result = ""
    carry = ""
    add = ""
    #faz a soma dos bits
    for i in range(0, len(num_bit)):
        if num_bit[i] == '1' and den_bit[i] == '1':
            add = '0'
            carry = '1'
        elif num_bit[i] == '0' and den_bit[i] == '1':
            add = '1'
            carry = '0'
        elif num_bit[i] == '1' and den_bit[i] == '0':
            add = '1'
            carry = '0'
        elif num_bit[i] == '0' and den_bit[i] == '0':
            add = '0'
            carry = '0'
        #faz a propagacao do carry
        if carry == '1':
            if add == '1':
                result += '0'
                carry = '1'
            else:
                result += '1'
        else:
            result += add

    #add + 1
    i = len(result) - 1
    carry = '1'
    while i >= 0:
        if carry == '1':
            if result[i] == '0':
                result[i] == '1'
                carry = '0'
                break
            else:
                result[i] == '0'
                carry = '1'
        i -= 1
    print (result)
    result = int(result, 2)
    return result

#Divisao --- entrada (dividendo, divisor) ; saida (quociente, resto)
def divid(op1, op2):
   
    dividendo = [int(a) for a in op1]
    divisor = [int(b) for b in op2]

    if dividendo == divisor:
        return (1,0)
    elif len(dividendo) < len(divisor):
        print ("Erro: Divisor maior que o dividendo")
        return (0,0)
    elif len(dividendo) == len(divisor) and dividendo < divisor:
        print ("Erro: Divisor maior que o dividendo")
        return (0,0)
    elif len(divisor) == 1 and divisor[0] == [0]:
        print ("Erro: Impossivel divisao por 0")
        return (0,0)

    min = [1]
    max = dividendo
    mid = [] 
    mid = [9 for i in range(1, len(max))]
    mid.append(int(max[0]/2))
    mid.reverse()
    quociente = 0
    resto = 0
    while True:           
        #multiplica para ver se chegou a uma aproximação do dividendo
        quociente = multiplication(mid, divisor)
        while quociente[0] == 0: quociente.pop(0)      
        #calcula o resto da divisao
        resto = minus2(dividendo, quociente)
        while resto[0] == 0 and len(resto) > 1 : resto.pop(0) 
        #se o dividendo é igual o resultado da multiplicacao o valor esta correto
        if dividendo == quociente:
            mid = toString(mid)
            return (mid, '0')
        #se o resto da divisao for menor que o divisor encontrou o numero
        elif len(resto) == len(divisor) and resto < divisor or len(resto) < len(divisor):
            mid = toString(mid)
            resto = toString(resto)
            return (mid, resto)
        elif len(dividendo) == len(quociente) and dividendo > quociente:
            mid[-1] = mid[-1] + 1
            min = carryOver(mid)
        elif len(dividendo) > len(quociente):
            mid[-1] = mid[-1] + 1
            min = carryOver(mid)
        elif len(dividendo) == len(quociente) and dividendo < quociente:
            mid[-1] = mid[-1] - 1
            max = carryOver(mid)
        elif len(dividendo) < len(quociente):
            mid[-1] = mid[-1] - 1
            max = carryOver(mid)
        
        while max[0] == 0: max.pop(0)
        mid = []
        if len(max) > 1:    
            mid = [9 for i in range(1, len(max))]
        mid.append(int(max[0]/2))
        mid.reverse()
        while mid[0] == 0: mid.pop(0)
        if len(min) == len(mid) and min > mid or len(min) > len(mid):
            mid = min

def toString(var):
    s = ''
    for i in var:
         s += str(i)
    return s

#Exponenciacao utilizando exponenciação por squaring ref: https://en.wikipedia.org/wiki/Exponentiation_by_squaring
def exp_by_squaring(x, n):
    return exp_by_squaring2(1, int(x), int(n))

def exp_by_squaring2(y, x, n):
    if n < 0:
        return exp_by_squaring2(y, 1/x, - n)
    elif n == 0:
        return y
    elif n == 1:
        return x * y
    elif n % 2 == 0:
        return exp_by_squaring2(y, x * x, n / 2)
    elif n % 2 != 0:
        return exp_by_squaring2(x * y, x * x, (n - 1) / 2)

#Inverso Multiplicativo ref https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def inverse(a, n):
    t = '0'
    oldt = newt = '1'    
    r = n
    oldr = newr = a
    
    while newr != '0':
        aux = divid(r, newr)
        quotient = aux[0]
        
        (r, newr) = (newr, toString(minus3(r, toString(multiplication(quotient, newr)))))       
        (t, newt) = (newt, toString(minus3(t, toString(multiplication(quotient, newt)))))

    if int(r) > 1:
        return "Operando " + a + " nao e invertivel com modulo " + n
    if int(t) < 0:
        t = sum(t, n)  
    
    inv = int(n) - int(t)
    
    if(int(a) * inv) % int(n) == 1:
        print ("Invertivel " + a + " modulo " + n)
    
    return (inv)

def algorithm_Ditfie_Hellmann(num, n):
    a = random.choice(range(0,int(n)))
    print ("Valor de A: ", a)
    b = random.choice(range(0,int(n)))
    print ("Valor de B: ", b)

    resB = exp_by_squaring(exp_by_squaring(num, a) % int(n), b) % int(n)
    resA = exp_by_squaring(exp_by_squaring(num, b) % int(n), a) % int(n)

    if resA == resB:
        print ("Valor criptografado: " + str(resA))

    
while True:
    option = menuPrincipal()
    if option == '1':
        op1 = menuOperando()
        op2 = menuOperando()
        res = sum(op1, op2)
        print ("Result: ")
        print (res)

    elif option == '2':
        op1 = menuOperando()
        op2 = menuOperando()
        res = multiplication(op1, op2)
        print ("Result: ")
        print (res)

    elif option == '3':
        op1 = menuOperando()
        op2 = menuOperando()
        res = divid(op1, op2)
        print ("Result: ")
        print (res)

    elif option == '4':
        op1 = menuOperando()
        op2 = menuOperando()
        res = exp_by_squaring(op1, op2)
        print ("Result: ")
        print (res)

    elif option == '5':
        op1 = menuOperando()
        op2 = menuOperando()
        res = minus(op1, op2)
        print ("Result: ")
        print (res)

    elif option == '6':
        op1 = menuOperando()
        op2 = menuOperando()
        res = inverse(op1, op2)
        print ("Result: ")
        print (res)

    elif option == '7':
        op1 = menuOperando()
        op2 = menuOperando()
        res = algorithm_Ditfie_Hellmann(op1, op2)

    elif option == '8':
        break
