"""
Faça um programa que pergunte a hora ao usuário e, baseando no horario 
descrito, exiba a saudação apropriada.
Ex: 
Bom Dia 0-11, Boa Tarde 12-17 e Boa Noite 18-23
"""

horas = input("Qual o horário de agora, Senhor(a)? ")

try:
    horas = int(horas)
    
    if 0 <= horas <= 11:
        print("Bom dia, Senhor(a)!")
    elif 12 <= horas <= 17:
        print("Boa tarde, Senhor(a)!")
    elif 18 <= horas <= 23:
        print("Boa noite, Senhor(a)!")
    else:
        print("Hora inválida. Por favor, insira um número entre 0 e 23.")
except:
    print("Isso não é um horário válido, Senhor(a).")
