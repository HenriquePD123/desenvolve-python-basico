# entrada
genero = input("Genero(m/f): ")
idade = int(input("Idade: "))
tempo_trabalho = int(input("Tempo de trabalho: "))
# processamento
a = (genero == 'f' and idade >= 60) or (genero == 'm' and idade >= 65)
b = tempo_trabalho > 30
c = idade >= 60 and tempo_trabalho >= 25
pode_aposentar = a or b or c
# saida
print(pode_aposentar)
