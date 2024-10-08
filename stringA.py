# Função para verificar a existência da letra 'a' (maiúscula ou minúscula) e contar sua ocorrência
def check_letter_a(string):
    # Contagem de ocorrências de 'a' ou 'A'
    count = string.lower().count('a')
    
    # Verificar se a letra 'a' aparece e retornar a quantidade
    if count > 0:
        return f"A letra 'a' aparece {count} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

if __name__ == "__main__":
    # Definindo a string para verificar
    texto = "A banana é uma fruta muito gostosa."
    # Chamando a função
    print(check_letter_a(texto))
