# Função para inverter uma string
def inverter_string(s):
    # Inicializa uma string vazia para armazenar o resultado
    string_invertida = ""
    
    # Percorre a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]  # Adiciona cada caractere à nova string

    return string_invertida

# Entrada da string pelo usuário
string_original = input("Digite a string que deseja inverter: ")

# Se preferir, você pode descomentar a linha abaixo e definir uma string diretamente
# string_original = "Exemplo de string"

# Inverte a string
resultado = inverter_string(string_original)

# Exibe o resultado
print(f"String original: {string_original}")
print(f"String invertida: {resultado}")
