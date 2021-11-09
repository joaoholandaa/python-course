npts = int(input("Quantidade de instantes de tempo: "))
pts = range(0,npts)


#Variável que define o intervalo de tempo
dt = float(input("Digite o valor do intervalo de tempo: "))

t_lista=[]

for i in pts:
	t_lista.append(i*dt)

#aceleração
a = float(input("digite o valor da aceleração: "))

traj_lista=[]
for t in t_lista:
	x=a*t**2/2
	traj_lista.append([t,x])

dico = {'assunto':'muv', 'aceleracao':a, 'movimento':traj_lista}
print(dico['assunto'])

print("aceleracao: {0:.2f} m/s**2".format(dico['aceleracao']))

for i in dico['movimento']:
	print("t = {0:.2f}s ; x = {1:.3f} m".format(i[0],i[1]))