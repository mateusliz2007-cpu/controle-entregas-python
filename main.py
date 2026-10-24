print("="*40)
print("SISTEMA DE GESTÃO DE ENTREGAS")
print("="*40)
print("Bem-Vindo ao Sistema!")

while True:
    try:
        quantidade_entregas = int(input("Quantidade de entregas para registrar: "))
        if quantidade_entregas <= 0:
            print("Valor Incorreto")
        else: 
            break

    except ValueError:
        print("Entrada Inválida! Digite um número inteiro: ")

print(f"Serão cadastradas {quantidade_entregas} entregas.")

#listas
cliente = []
cidade = []
distancia = []
peso = []
valor = []

#Funação para fromatar números
def formatar_numero(valor):
    numero_formatado = f"{valor:,.2f}"
    numero_formatado = numero_formatado.replace("," , "X")
    numero_formatado = numero_formatado.replace(".", ",")
    numero_formatado = numero_formatado.replace("X" , ".")
    return numero_formatado


for i in range(quantidade_entregas):
    cliente.append(str(input("Cliente: ")))
    cidade.append(str(input("Cidade: ")))
    while True:
        try:
            distancia_digitada = float(input("Distância(Km): "))
            if distancia_digitada <= 0:
                print("Valor Incorreto")
            else:
                distancia.append(distancia_digitada)
                break
        except ValueError:
            print("Entrada inválida, Digite Novamente: ")
    
    while True:
        try:
            peso_digitado = float(input("Peso(kg): "))
            if peso_digitado <=0:
                print("Valor Inválido")
            else:
                 peso.append(peso_digitado)
                 break
        except ValueError:
            print("Entrada Inválida, Digite Novamente: ")
        
    while True:
        try:
            valor_digitado = float(input("Valor(R$): "))
            if valor_digitado <= 0:
                print("Valor Inválido")
            else:
                valor.append(valor_digitado)
                break
        except ValueError:
            print("Entrada Inválida, Digite Novamente: ")
            

#Totais
total_valor = sum(valor)
total_distancia = sum(distancia)
total_peso = sum(peso)

print("="*30)
print("RESUMO OPERACIONAL")
print("="*30)

print(f"Entregas Registradas: {quantidade_entregas}")
print(f"Valor Total: R$ {formatar_numero(valor=total_valor)}")
print(f"Distância Total: {formatar_numero(valor=total_distancia)} Km")
print(f"Peso Total: {formatar_numero(valor=total_peso)} Kg")

#Médias
media_valor = total_valor/quantidade_entregas
media_distancia = total_distancia/quantidade_entregas
media_peso = total_peso/quantidade_entregas

print("="*30)
print("MÉDIAS POR ENTREGA")
print("="*30)

print(f"Valor Médio: R$ {formatar_numero(valor=media_valor)}")
print(f"Distância Média: {formatar_numero(valor=media_distancia)} Km")
print(f"Peso Médio: {formatar_numero(valor=media_peso)} Kg")

#Maiores
maior_valor = max(valor)
indice_maior_valor = valor.index(maior_valor) + 1

maior_distancia = max(distancia)
indice_maior_distancia = distancia.index(maior_distancia) + 1

maior_peso = max(peso)
indice_maior_peso = peso.index(maior_peso) + 1

print("="*30)
print("MAIORES INDICADORES")
print("="*30)
print(f"Maior Distância: {formatar_numero(valor=maior_distancia)} Km, Entrega: {indice_maior_distancia}")
print(f"Maior Valor: R$ {formatar_numero(valor=maior_valor)}, Entrega {indice_maior_valor}")
print(f"Maior Peso: {formatar_numero(valor=maior_peso)} Kg, Entrega: {indice_maior_peso}")


for r in range(quantidade_entregas):
    print("="*30)
    print(f"RELATÓRIO INDIVÍDUAL {r+1}")
    print("="*30)
    print(f"Cliente: {cliente[r]}")
    print(f"Cidade: {cidade[r]}")
    print(f"Distância: {formatar_numero(distancia[r])} Km")
    print(f"Peso: {formatar_numero(peso[r])} Kg")
    print(f"Valor: R$ {formatar_numero(valor[r])}")
    
    valor_por_km = valor[r]/distancia[r]
    print(f"Valor por Km: {formatar_numero(valor_por_km)}, Rota {r+1}")

    valor_por_kg = valor[r]/peso[r]
    print(f"Valor por Kg: {formatar_numero(valor_por_kg)}, Rota {r+1}")



