import random
import string

from numpy import character

pergunta_senha = int(input("Quantos caracteres a senha deve ter?: "))

if pergunta_senha <= 0:
    print("A senha deve ter pelomenos 1 caracter")
    exit()


print("Escolha um tipo de senha:")
print("1 - Somente letras")
print("2 - letras e números")
print("3 - letras , números e símbolos")
tipo = int(input("Opção: "))

if tipo == 1:
    caracteres = string.ascii_letters
elif tipo == 2:
    caracteres = string.ascii_letters + string.digits
elif tipo == 3:
    caracteres = string.ascii_letters + string.digits + string.punctuation
else:
    print("Erro! Digite um numero valido")
    caracteres = string.ascii_letters + string.digits + string.punctuation

senha_feita = ''.join(random.choice(caracteres) for _ in range(pergunta_senha))


print(senha_feita)
