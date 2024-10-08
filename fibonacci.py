# Função para gerar a sequência de Fibonacci até um limite
def is_in_fibonacci(n):
    fib_seq = [0, 1]
    
    # Gerar a sequência até que o próximo valor seja maior ou igual ao número informado
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    # Verificar se o número informado pertence à sequência
    if n in fib_seq:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

if __name__ == "__main__":
    # Definindo o número para verificar
    numero = 34
    # Chamando a função
    print(is_in_fibonacci(numero))
