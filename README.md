# Задания ЕГЭ
 + [Задание 2](#num2);
 + [Задание 8](#num8);
 + [Задание 12](#num12);
 + [Задание 14](#num14);
 + [Задание 15*](#num15);
 + [Задание 16](#num16);
 + [Задание 17](#num17);
 + [Задание 19-21](#num1921);
 + [Задание 23](#num23);
 + [Задание 24](#num24);
 + [Задание 25](#num25);

# Коды
+ [Перевод систем счисления (Python)](#code1);

-----------------------------

<br/>

-----------------------------

## <a name="num2"></a> Задание 2
Логическая функция F задаётся выражением (a → b) ∧ ¬(b ≡ c) ∧ (d → a). На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся наборы аргументов, при которых функция F истинна. Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных a, b, c, d.
В ответе напишите буквы a, b, c, d в том порядке, в котором идут соответствующие им столбцы. Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.
![image](https://user-images.githubusercontent.com/88733735/140971738-94e37714-06fd-4c06-95b4-83e0e7e216c8.png)

```python
for a in range(0,2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                if ((not(a) or b) and not (b == c) and (not(d) or a)):
                    print(a,b,c,d)
```
```python
# импликация - not(a) or b
```
--------------------------------------------------

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
# импликация - not(a) or b      !!!
```

--------------------------------------------------

## <a name="num16"></a> Задание 16
Алгоритм вычисления значения функции F(n), где n – целое число, задан следующими соотношениями:<br/>
_F(0) = 0 <br/>
F(n) = F(n/2), при чётном n > 0<br/>
F(n) = F(n - 1) + 3, при нечётном n > 0<br/>_
Сколько существует значений n, принадлежащих отрезку [1; 1000], для которых F(n) равно 18?<br/>
```python
def f(n):
    if n == 0:
        return 0
    elif n > 0 and n%2 == 0:
        return f(n/2)
    elif n > 0 and n%2!=0:
        return f(n-1) + 3
count = 0
for i in range(1,1000+1):
    if f(i) == 18:
        count+=1
print(count)
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


### ! - альтернативное чтение файла
```python
f = open('17.txt')
a = list(map(int, f.read().split()))
```

[Больше примеров](https://github.com/HrtLock/EGE/blob/main/17.md "Примеры задания 12")

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
**Тип заданий 1**
Найти сколько чисел можно получить на участке от 1 до 40 не включая число 12
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
**Тип заданий 2**
Исполнитель Калькулятор преобразует число, записанное на экране в троичной системе счисления. У исполнителя есть две команды, которым присвоены номера:<br>
1. Прибавь 2<br>
2. Умножь на 2 и прибавь 1<br>
Сколько различных результатов можно получить из исходного числа 2 после выполнения программы, содержащей ровно 15 команд?
```python
arr = []
def f (x,p):
    if p == 15:
        if not x in arr:
            arr.append(x)
    if p < 15:
        f(x+2, p+1)
        f(x*2+1, p+1)
f(2,0)
print(len(arr))
```

--------------------------------------------------

## <a name="num24"></a> Задание 24
**Тип заданий 1** <br>
Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите длину самой длинной последовательности, состоящей из символов X. Хотя бы один символ X находится в последовательности.
```python
with open('24_demo.txt', 'r') as file:
    s = file.readline()
    k = 1
    for k in range(1,60):
        if "X"*k in s:
            print(k)
```

**Тип заданий 2** <br>
Текстовый файл 24-171.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита (ABC…Z). Файл разбит на строки различной длины. Определите максимальную длину цепочки символов, состоящей из повторяющихся фрагментов XYZ. Цепочка должна начинаться с символа X и заканчиваться символом Z. Например, для строки SAZZXYZXYZXZQW длина цепочки равна 6: XYZ+XYZ.

```python
f = open('24.txt')
a = list(map(str, f.read().split()))
cnt = 0
max = 0
for i in range(len(a)):
    for j in range(len(a[i])-2):
        if (a[i][j] == 'X' and cnt%3==0) or (a[i][j] == 'Y' and cnt%3==1) or (a[i][j] == 'Z' and cnt%3==2):
            cnt +=1
            if cnt > max:
                max = cnt
        else:
            cnt = 0
print(max)
```


--------------------------------------------------

## <a name="num25"></a> Задание 25
Список всех делителей числа
```python
def deli(n):
    d = 2
    sp = []
    while d * d < n:
        if n % d == 0:
            sp.append(d)
            if d != n // d:
                sp.append(n // d)
        d += 1
```
```python
    return sorted(sp)[:5] //возвращает первые 5 минимальных делителей
```


**Один из типов заданий**
Обозначим через M разность максимального и минимального числа среди простых делителей целого числа, не считая самого числа. Если таких делителей у числа нет, то считаем значение M равным нулю. Напишите программу, которая перебирает целые числа, большие 450000, в порядке возрастания и ищет среди них такие, для которых значение M при делении на 29 даёт в остатке 11. Выведите первые 4 найденных числа в порядке возрастания, справа от каждого числа запишите соответствующее значения M.

```python
#функция возвращает все делители числа
def deli(n):
    d = 1
    sp = []
    while d * d < n:
        if n % d == 0:
            sp.append(d)
            if d != n // d:
                sp.append(n // d)
        d += 1
    return sorted(sp)

num = 450000
cnt = 0
while True:
    min = 9999999
    max = 0
    dels = deli(num)
    for x in dels:
        if len(deli(x)) == 2:
            if x < min:
                min = x
            if x > max:
                max = x
    m = max-min
    if m%29==11:
        print(num, m)
        cnt += 1
    num+=1
    if cnt == 4:
        break
```

**Один из типов заданий**
Пусть M (N) – сумма двух наибольших различных натуральных делителей 
натурального числа N, не считая самого числа. Если у числа N меньше двух 
таких делителей, то M (N) считается равным 0.
Найдите 5 наименьших натуральных чисел, превышающих 10 000 000, для 
которых 0 < M (N) < 10 000.
В ответе запишите найденные значения M (N) в порядке возрастания 
соответствующих им чисел N
```python
def f (x):
    d = 2
    arr = []
    while d ** 2 < x:
        if x % d == 0:
            arr.append(d)
            if d != x//d:
                arr.append(x//d)
        d += 1
    return sorted(arr)[-2:]
cnt=0
for i in range (10000000, 1000000000):
    st = f(i)
    if len(st) != 0:
        m = st[0] + st[1]
        if m < 10000:
            print(m)
            cnt+=1
        if cnt == 5:
            break
```
-----------------------------




-----------------------------

## <a name="code1"></a> Перевод систем счисления (Python)
```python
n = int(input('Число '))
a = int(input('Из '))
b = int(input('B '))

if b != a:
    n = int(str(n), a)
    num = ''
    while n > 0:
        if n % b>=10:
            add = chr((n % b)+55)
        else:
            add = str(n % b)
        num = add + num
        n //= b
else :
    num = n
print(num)
```
