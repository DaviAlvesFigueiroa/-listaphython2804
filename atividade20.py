#Valor absoluto(sem sinal)
num = float(input("Digite um numero:"))

if num < 0:
    absoluto = num * -1 
else:
    absoluto = num
print(f"O valor absoluto (sem o sinal) e: {absoluto}")