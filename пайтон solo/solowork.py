import numpy as np

def detx(x, mz, mr):
    mzbuff=np.copy(mz)
    mrbuff=np.copy(mr)
    for i in range(len(mrbuff)):
        mzbuff[i][x]=mrbuff[i]
    return mzbuff

mat = []
matrez = []

size = int(input("Введите количество неизвестных переменных: "))
print("\n")
for i in range(size):
    mat.append([])
    for j in range(size):
        mat[i].append(int(input(f"Введите {j+1}-й коэффицент {i+1}-й строки: ")))
    matrez.append(int(input(f"Введите результат {i+1}-й строки: ")))
    print("\n")

for i in range(size):
    print(f"x{i+1} = {round(np.linalg.det(detx(i, mat, matrez))/np.linalg.det(mat), 2)}")