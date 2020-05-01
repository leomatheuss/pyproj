import os
from dice import random_dice

def regras():
    return print("Escolha qual tipo de dado você quer utilizar, e quantas vezes você vai querer rodar aquele dado, você também pode escolher mais de um dado\nDados permitidos: D4,D6,D8,D10,D12,D20")

def play1():
    print('-'*50)
    print("Deseja rolar quantos dados?")
    print('-'*50)
    n = int(input())
    os.system('clear')
    print("Quais dados você deseja rolar?")
    j = 0
    for i in range(1,n+1):
        k = int(input())
        
        j = j + random_dice(k) 
        print("Roll nº",i,"=", random_dice(k))


    print("Você rolou um total de",n,"dados, sendo a soma deles de:",j)

def main():
    print("-"*60)
    print(" "*15, "Bem vindo ao DADO virtual")
    print("-"*60)
    print('')
    print("Para começar digite 1.\nPara entender como utilizar, pressione 2\nPara sair pressione 0")
    t = int(input())
    if t == 0:
        pass
    elif t == 2:
        os.system('clear')
        regras()
        print('-'*100)
        print('-'*100)
        main()
    elif t == 1:
        os.system('clear')
        play1()
    else:
        pass

main()