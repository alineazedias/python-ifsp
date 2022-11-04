cadastrados = 0
aprovados = 0
exame = 0
reprovados = 0
totalFemAprovado = 0
totalMascAprovado = 0
totalFemExam = 0
totalMascExam = 0
totalFemReprovado = 0
totalMascReprovado = 0

cadastro = input ("Deseja se cadastrar?(S/N): ").upper()
while (cadastro != "S" and cadastro != "N"):
    print("Opção Inválida! Tente novamente")
    cadastro = input ("Deseja se cadastrar?: ").upper()

while (cadastro == "S"):
    cadastrados += 1
    nome = input("Digite seu nome: ")
    sexo = input("Digite o sexo(F/M): ").upper()

    while (sexo != "F" and sexo != "M"):
        print("Sexo inválido")
        sexo = input("Digite F - Feminino ou M - Masculino: ").upper()

    print(f"Olá " +nome.upper()+ ", informe suas notas abaixo: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3
    print(f"Sua média é: "+str(media))
   
    if (media >=7):
        print("Você está aprovado!")
        aprovados += 1

    elif (media >=4 and media <7):
        print("Você está de recuperação!")
        exame +=1
    else:
        print("Você está reprovado!")
        reprovados +=1

    if (sexo == "F" and media >= 7):
        totalFemAprovado += 1
    elif(sexo == "F" and media >=4 and media <7):
        totalFemExam += 1
    elif(sexo == "F" and media <4):
        totalFemReprovado += 1
    elif (sexo == "M" and media >= 7):
        totalMascAprovado += 1
    elif(sexo == "M" and media >=4 and media <7):
        totalMascExam += 1
    elif(sexo == "M" and media <4):
        totalMascReprovado += 1

    continuar =input('Continuar?(S/N): ').upper()
    if (continuar != "S" and continuar != "N"):
        print("Opção Inválida! Tente novamente")
        continuar = input('Digite S - Sim ou N - Não: ')
    elif (continuar == "N"):
        break
    

print("Resultado")

print(f"Total alunos cadastrados: ", cadastrados)
print(f"Total alunos aprovados: ", aprovados)
print(f"Total alunos de exame: ", exame)
print(f"Total alunos reprovados: ", reprovados)
print(f"Total mulheres aprovadas: ", totalFemAprovado)
print(f"Total homens aprovados: ", totalMascAprovado)
print(f"Total mulheres de exame: ", totalFemExam)
print(f"Total homens de exame: ", totalMascExam)
print(f"Total mulheres reprovadas: ", totalFemReprovado)
print(f"Total homens reprovados: ", totalMascReprovado)

print(f"Porcentagem dos alunos aprovados: {aprovados*100/cadastrados}%")
print(f"Porcentagem dos alunos em recuperação: {exame*100/cadastrados}%")
print(f"Porcentagem dos alunos reprovados: {reprovados*100/cadastrados}%")