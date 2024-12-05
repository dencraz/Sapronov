# Дан список A размера N и целое число K (1 < K < 4, K < N ).
# Осуществить циклический сдвиг элементов списка влево на K позиций (при этом AN перейдет в AN_K, AN-1 — в AN-K-1, ..., A1 — в AN-K+1).
# Допускается использовать вспомогательный список из 4 элементов.
def find_positions(N, K):
    positions = []
    for i in range(N):
        positions.append((i + K) % N)
    return positions

# Пример использования
N = int(input("Введите N"))
K = int(input("Введите K"))
positions = find_positions(N, K)
print(positions)