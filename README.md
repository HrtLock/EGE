# Задания ЕГЭ

 + [Задание 12](#num12);
 + [Задание 14](#num14);
 + [Задание 15*](#num15);
 + [Задание 19-21](#num1921);
 + [Задание 23](#num23);
 + [Задание 24](#num24);

## <a name="num12"></a> Задание 12

Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 84 единиц?

НАЧАЛО<br/>
 &nbsp; &nbsp; ПОКА нашлось (11111)<br/>
 &nbsp; &nbsp;&nbsp; &nbsp; заменить (222, 1)<br/>
 &nbsp; &nbsp;&nbsp; &nbsp; заменить (111, 2)<br/>
 &nbsp; &nbsp; КОНЕЦ ПОКА<br/>
КОНЕЦ<br/>

```python
x = '1'*84
while '11111' in x:
    x = x.replace('222', '1',1)
    x = x.replace('111', '2',1)
print(x)
```
> output - 222111

[Больше примеров](https://github.com/DazzS/ege/blob/main/12.md "Примеры задания 12")

--------------------------------------------------

## <a name="num14"></a> Задание 14
Укажите наименьшее основание системы счисления, в которой запись числа 50 трехзначна.

Максимальное <b>трехзначное</b> число в <b>n-ичной</b> системе равно <b>n<sup>3</sup> − 1</b>. <br/>
Это число не меньше 50 <i>(по условию)</i>, а поэтому n не меньше 4. 
 > Следовательно, наименьшее n = 4.

[Больше примеров (с решением выражений)](https://github.com/DazzS/ege/blob/main/14.md "Примеры задания 14")

--------------------------------------------------

## <a name="num15"></a> Задание 15*
Для какого наибольшего целого числа А формула <br/>
&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;((x ≤ 9) →(x ⋅ x ≤ A)) ⋀ ((y ⋅ y ≤ A) → (y ≤ 9)) <br/>
тождественно истинна, то есть принимает значение 1 при любых целых неотрицательных x и y?

```python
def f(x,y,a):
    return ((x <= 9) <= ((x*x) <= a)) and (((y*y)<=a) <= (y <=9))

for a in range(1, 1000):
    fl = True
    for x in range(1,1000):
        for y in range(1,1000):
            
            if not(f(x, y, a)) :
                fl = False
                break #Если x и y не подходят, то выходим из цикла
        if fl == False:
            break
    if fl:
        print(a)
```
> output - 81 82 83 ... 97 98 99<br/>
> Ответ: 99

[Больше примеров](https://github.com/DazzS/ege/blob/main/15.md "Примеры задания 15")

[Задание 15. Законы алгебры логики](https://user-images.githubusercontent.com/49374948/121887595-986ea380-cd1f-11eb-8d0c-3bd66523003e.png)

```python
# *решение не всегда верное
```

--------------------------------------------------

## <a name="num1921"></a> Задание 19-21 - Теория игр

### №19
```python
def f(x, y, p):
    if x + y >= 84 and p == 3: # Выигрыш на 3-ем ходу игры
        return True
    elif x + y < 84 and p == 3: # Проигрыш на 3-ем ходу игры
        return False
    return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 3, p + 1)
    # При каком-либо исходе игры игрок выигрывает


for i in range(1, 67 + 1):
    if f(16, i, 1):
        print(i)
        break
```

### №20
```python
def f(x, y, p):
    if x + y >= 84 and p == 4: # Выигрыш на 4-ом ходу игры
        return True
    else:
        if x + y < 84 and p == 4: # Проигрыш на 4-ом ходу игры
            return False
        elif x + y >= 84: # Выигрыш на ином ходу игры
            return False

    if p % 2 == 1:
        return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 3, p + 1)
        # При каком-либо исходе игрока 1, игрок выигрывает
    else:
        return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 3, p + 1)
        # При любом исходе игрока 2 , игрок выигрывает

for i in range(1, 67 + 1):
    if f(16, i, 1):
        print(i)


```

### №21
```python
def f(x, y, p):
    if x + y >= 84 and (p == 3 or p == 5): # может выиграть на 3 или 5 ходу
        return True
    else:
        if x + y < 84 and p == 5: # не может проиграть на 5-ом ходу
            return False
        elif x + y >= 84:
            return False

    if p % 2 == 0:
        return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 3, p + 1)
        # При каком-либо исходе игрока 2, игрок выигрывает
    else:
        return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 3, p + 1)
        # При любом исходе игрока 1 , игрок выигрывает

for i in range(1, 67 + 1):
    if f(16, i, 1):
        print(i)

```

--------------------------------------------------

## <a name="num23"></a> Задание 23

```python
def f(x, y):   # Путь из числа X и Y
    if x == y:   # X попал в Y
        return 1
    if x > y or x == 14:   # X больше игрика и НЕ должен проходить через 14 (выбитая точка)
        return 0
    if x < y:
        return f(x + 1, y) + f(x * 2, y) + f(x * 3, y) # Все возможные действия


print(f(1, 12) * f(12, 40)) # Умножение - обязательное попадание точки 12 на пути 

```

--------------------------------------------------

## <a name="num24"></a> Задание 24
Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите длину самой длинной последовательности, состоящей из символов X. Хотя бы один символ X находится в последовательности.
```python
with open('24_demo.txt', 'r') as file:
    s = file.readline()
    k = 1
    for k in range(1,60):
        if "X"*k in s:
            print(k)
```
