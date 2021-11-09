a = 10
b = 25
c = 66

x = int(input("Digite um número: "))

if(x == a or x == b or x == c): #ou if(x in [a,b,c]):
    print("Está contido")
else:
    print("Não está contido")

cores = ["azul","amarelo","vermelho","branco"]

while True:
    cor = input("Digite o nome de uma cor ou então,"
                " O para sair do programa: ")

    if(cor=="O"):
        break
    elif cor in cores:
        print("Essa cor está contida")
    else:
        print("Essa cor não está contida")
    print()