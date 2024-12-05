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