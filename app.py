# Entrada da variável matéria
materia = input("Nome da matéria: ")
materiaLower = materia.lower()

# Verificação de dados inseridos pelos usuário
while True:
    try:
        cargaH = int(input(f"Carga Hóraria da matéria {materiaLower}: "))
        
        if cargaH <= 0 :
                print("A carga horária e as faltas ser valores positivos. Tente novamente.")
                continue
            
        faltas = int(input(f"Quantidade de Faltas da matéria {materiaLower}: "))
        if faltas <= 0:
                print("As faltas devem ser valores positivos. Tente novamente.\n") # \n para separar os erros anterios com a nova entrada de dados
                continue
        break
    except ValueError:
            print("Por favor, insira um número(s) válido(s).")
# Variáveis a receber

# Cálculos

cargaHemM = cargaH * 60 # Carga horária em minutos, ou seja, multiplica-se por 60 minutos
qtdAulas = cargaHemM / 50 # Horas em minuto, com a carga horária convertida em minutos, multiplicamos por 50 para saber a quantidade de aulas
vcpDaMat = cargaH * 0.25 # Vinte cinco porcento da máteria pra saber o limiar de decisão

# Condições

if faltas < vcpDaMat : 
    podeFaltar = vcpDaMat - faltas # 10 é a quantidade máxima faltas que pode ter na matéria de 40h
    print(f"\nA matéria de {materiaLower} tem {cargaH} horas e há {qtdAulas:.0f} aulas") # O usuário ainda pode faltar
    print(f"E você pode faltar {podeFaltar:.0f} aulas")
        
if faltas == vcpDaMat :
    print(f"\nA matéria de {materiaLower} tem {cargaH} horas e há {qtdAulas:.0f} aulas")
    print(f"Você não pode mais faltar") # O usuário está no limite máximo de faltas
        
if faltas > vcpDaMat :
    faltasAmais = faltas - vcpDaMat # Diferença de quantas vezes o usuário faltou a mais do que o permido
    
    print(f"\nA matéria de {materiaLower} tem {cargaH} horas e há {qtdAulas:.0f} aulas")
    print(f"Você passou de {vcpDaMat} faltas permitidas com {faltasAmais:.0f} faltas a mais do permitido")
    # O usuário perdeu na máteria por faltas

# Término do calculo -----------------------------------