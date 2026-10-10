# Aprendizagem e revisão da linguagem Python

#Comentário: descreve a intenção do trecho do código-fonte
print("Olá, Python!")
print("A soma é:", (3 + 5))
print("\n")
nome = "Ana"
idade = 17
altura = 1.65
matriculado = True

for valor in [nome, idade, altura, matriculado]:
    print(valor, type(valor))

print("\n")

#Entrada de dados e conversão
nome = input("nome: ")
idade = int(input("idade: "))
print(F"{nome} terá {idade + 1} anos no próximo aniversário!")
print("Tipo do nome:", type(nome))
print("\n")

#Operações aritméticas
a, b = 10, 3
print((a+b), (a-b), (a*b))
print((a/b), (a // b), (a % b), (a ** b))
print("Par?", 12 % 2 == 0 )
print("\n")

idade = 19
autorizado = True
print(idade) 
print(idade >=18 and autorizado)
print(idade < 18 or not autorizado)
print(idade == 19, idade != 19)
print("\n")

#Decisões com iif, else e else
nota = float(input("Nota: "))
if nota >= 7:
    print("Aprovado, parabéns!")

elif nota >= 5:
    print("Cuidado, recuperção!")

else:
    print("Infelizmente foi reprovado!")