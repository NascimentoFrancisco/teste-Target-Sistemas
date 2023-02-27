
def fibonacci_sequence(num) -> list:
    """Função que retorna a sequência de Fibonacci até o número informado."""
    a, b = 0, 1
    sequence = list()
    while a <= num:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def is_fibonacci(num) -> bool:
    """Função que verifica se um número pertence à sequência de Fibonacci."""
    sequence = fibonacci_sequence(num)
    return num in sequence

num = int(input("Informe um número: "))
sequence = fibonacci_sequence(num)

print(f"Sequência de Fibonacci até o número informado: {sequence}")

if is_fibonacci(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"num não pertence à sequência de Fibonacci.")
