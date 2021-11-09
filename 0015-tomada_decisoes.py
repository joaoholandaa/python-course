a = 5
if(a==10):
    print("O valor de a é igual a 10")
elif(a==20):
    print("a é igual a 20 e não 10")
else:
    print("Não é nenhum dos dois")

acao = int(input("Digite '1' para sim e digite '2' para nao: "))
if(acao==1):
    print("Você disse que sim!")
else:
    if(acao==2):
        print("Você disse que não!")
    else:
        print("O número digitado não é '1' e nem '2'")