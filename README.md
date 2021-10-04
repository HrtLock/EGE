# Задания ЕГЭ

 + [Задание 8](#num8);
 + [Задание 12](#num12);
 + [Задание 14](#num14);
 + [Задание 15*](#num15);
 + [Задание 17](#num17);
 + [Задание 19-21](#num1921);
 + [Задание 23](#num23);
 + [Задание 24](#num24);

## <a name="num8"></a> Задание 8
Лиля составляет 5-буквенные слова из букв С, О, Т, К, А, П, Л, З. Слово не должно заканчиваться на гласную и содержать сочетания ЗЛО. Буквы в слове не повторяются. Сколько слов может составить Лиля?
```python

i = 'СОТКАПЛЗ'
count = 0
for a in i:
    for b in i:
        if a != b:
            for c in i:
                if c != a and c != b:
                    for d in i:
                        if d != a and d != b and d != c:
                            for e in i:
                                if e != a and e != b and e != c and e != d and e != 'О' and e != 'А':
                                    st = a + b + c + d + e
                                    if 'ЗЛО' in st:
                                        continue
                                    else:
                                        count += 1

print(count)

```
--------------------------------------------------

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

[Больше примеров](https://github.com/HrtLock/ege/blob/main/12.md "Примеры задания 12")

--------------------------------------------------

## <a name="num14"></a> Задание 14
Укажите наименьшее основание системы счисления, в которой запись числа 50 трехзначна.

Максимальное <b>трехзначное</b> число в <b>n-ичной</b> системе равно <b>n<sup>3</sup> − 1</b>. <br/>
Это число не меньше 50 <i>(по условию)</i>, а поэтому n не меньше 4. 
 > Следовательно, наименьшее n = 4.

[Больше примеров (с решением выражений)](https://github.com/HrtLock/ege/blob/main/14.md "Примеры задания 14")

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

[Больше примеров](https://github.com/HrtLock/ege/blob/main/15.md "Примеры задания 15")

[Задание 15. Законы алгебры логики](https://user-images.githubusercontent.com/49374948/121887595-986ea380-cd1f-11eb-8d0c-3bd66523003e.png)

```python
# *решение не всегда верное
```

--------------------------------------------------

## <a name="num17"></a> Задание 17
В файле содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от −10 000 до 10 000 включительно. Определите и запишите в ответе сначала количество пар элементов последовательности, в которых хотя бы одно число делится на 3, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности. Например, для последовательности из пяти элементов: 6; 2; 9; –3; 6 — ответ: 4 11.

```python
with open('17.txt', 'r') as f: # берем файл
    nums = f.read().splitlines() # заносим строки в массив (одна стрка = 1 элемент)
nums = [int(item) for item in nums]
count = 0
max = -20000
for i in range(0, len(nums)-1):
    if nums[i]%3==0 or nums[i+1]%3==0:
        count+=1
        if nums[i] + nums[i+1] > max:
            max = nums[i] + nums[i+1]
print(count, max)
```



В файле содержится последовательность из 10 000 целых положительных чисел. Каждое число не превышает 10 000. Определите и запишите в ответе сначала количество пар элементов последовательности, для которых произведение элементов не кратно 34, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

```python
with open('17_2.txt', 'r') as f: # берем файл
    nums = f.read().splitlines() # заносим строки в массив (одна стрка = 1 элемент)
nums = [int(item) for item in nums]
print(nums)

count = 0
max = 0
number = 0

for i in range(0, len(nums)):
    for j in range(number, len(nums)):
        if nums[i]*nums[j]%34!=0 and i != j:
            count+=1
            if nums[i]+nums[j] > max:
                max = nums[i]+nums[j]
    number+=1
print(count, max)
```
--------------------------------------------------

## <a name="num1921"></a> Задание 19-21 - Теория игр

Игрок 1 - P1, Игрок 2 - P2<br/><br/>

Порядок ходов ('p' в коде):<br/>
1 - Исходное<br/>
2 - P1<br/>
3 - P2<br/>
4 - P1<br/>
5 - P2<br/>
...

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
