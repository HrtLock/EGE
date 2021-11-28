n = 33
a = 7
b = 32
num = 40
print(f'Номер {num}.19')
def f(x, p):
    if x >= n and p == 3: # Выигрыш на 3-ем ходу игры
        return True
    elif x < n and p == 3: # Проигрыш на 3-ем ходу игры
        return False
    return f(x + 3, p + 1) or f(x * 2, p + 1)
    # При каком-либо исходе игры игрок выигрывает


for i in range(1, b + 1):
    if f(i, 1):
        print(i)
        break

print(f'Номер {num}.20')
def f(x, p):
    if x >= n and p == 4: # Выигрыш на 4-ом ходу игры
        return True
    else:
        if x < n and p == 4: # Проигрыш на 4-ом ходу игры
            return False
        elif x >= n: # Выигрыш на ином ходу игры
            return False

    if p % 2 == 1:
        return f(x + 3, p + 1) or f(x * 2, p + 1)
        # При каком-либо исходе игрока 1, игрок выигрывает
    else:
        return f(x + 3, p + 1) and f(x * 2, p + 1)
        # При любом исходе игрока 2 , игрок выигрывает

for i in range(1, b + 1):
    if f(i, 1):
        print(i)

print(f'Номер {num}.21')
def f(x, p):
    if x >= n and (p == 3 or p == 5): # может выиграть на 3 или 5 ходу
        return True
    else:
        if x < n and p == 5: # не может проиграть на 5-ом ходу
            return False
        elif x >= n:
            return False

    if p % 2 == 0:
        return f(x + 3, p + 1) or f(x * 2, p + 1)
        # При каком-либо исходе игрока 2, игрок выигрывает
    else:
        return f(x + 3, p + 1) and f(x * 2, p + 1)
        # При любом исходе игрока 1 , игрок выигрывает

for i in range(1, b + 1):
    if f(i, 1):
        print(i)



