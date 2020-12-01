g1 = 0
g2 = 0
g3 = 0

with open("votos.txt","w") as arquivo:
  for votos

print("\n----Seleção dos melhores trabalhos das AEP´s----\n")
print("Digite o grupo que deseja votar (1~3) ou -1 para sair:")
opcao = 0
while(opcao is not -1):
  opcao=int(input("-> Voto: "))
  if (opcao == 1):
    g1 = g1 + 1
  elif (opcao == 2):
    g2 = g2 + 1
  elif (opcao == 3):
    g3 = g3 + 1
  else:
    print("voto inválido")

total = g1+g2+g3
print("\n---Resultado---\n")
print(total, "votos")
print("Grupo 1:", g1)
print("Grupo 2:", g2)
print("Grupo 3:", g3)

maior = "1"

if (g1<g2):
  maior = "2"
elif (g1<g3):
  maior = "3"

if (g1 == g2 == g3):
  print("Não houver ganhador!")
else:
  print("O Grupo ganhador foi o grupo " , maior)

input("\nPressione enter...")
