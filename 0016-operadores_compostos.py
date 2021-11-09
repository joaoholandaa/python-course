idade = int(input("Informe sua idade:"))
if(idade<=0):
    print("Sua idade não pode ser igual ou menor do que 0!")
else:
    if(idade>150):
        print("Você não pode ter mais do que 150 anos!")
    else:
        if(idade<18):
            print("Você precisa ter mais do que 18 anos!")