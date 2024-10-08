import json

# Caminho para o arquivo JSON
arquivo_json = 'data/dados.json'

# Carregar os dados do arquivo JSON
with open(arquivo_json, 'r') as file:
    data = json.load(file)

# Inicializar variáveis para o cálculo
valores = [entry["valor"] for entry in data if entry["valor"] > 0]
total_faturamento = sum(valores)
num_dias_faturamento = len(valores)
media_mensal = total_faturamento / num_dias_faturamento if num_dias_faturamento > 0 else 0

# Cálculo do menor e maior valor de faturamento
menor_valor = min(valores) if valores else 0
maior_valor = max(valores) if valores else 0

# Contar os dias com faturamento superior à média
dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

# Resultados
print(f'Menor valor de faturamento: R${menor_valor:.2f}')
print(f'Maior valor de faturamento: R${maior_valor:.2f}')
print(f'Número de dias com faturamento acima da média: {dias_acima_media}')