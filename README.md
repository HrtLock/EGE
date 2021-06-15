# Задания ЕГЭ

 + [Задание 12](#num12);
 + [Задание 14](#num14);
 + [Задание 15](#num15);

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

## <a name="num15"></a> Задание 15
Для какого наибольшего целого неотрицательного числа A выражение<br/>
&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;(2x + 3y < 30) ∨ (x + y ≥ A)<br/>
тождественно истинно при любых целых неотрицательных x и y?

```python
for a in range(1, 1000):
    fl = True
    for x in range(1,1000):
        for y in range(1,1000):
            if not(((2*x + 3*y) < 30) or ((x + y) >= a)):
                fl = False
                break #Если x и y не подходят, то выходим из цикла
        if fl == False:
            break
    if fl:
        print(a)
```
> output - 1 2 3 4 5 6 7 8 9 10 (11)<br/>
> Ответ: 10

[Больше примеров](https://github.com/DazzS/ege/blob/main/15.md "Примеры задания 15")

[Задание 15. Законы алгебры логики](https://user-images.githubusercontent.com/49374948/121887595-986ea380-cd1f-11eb-8d0c-3bd66523003e.png)

--------------------------------------------------
