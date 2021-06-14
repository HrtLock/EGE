# Задания ЕГЭ с кодом


## Задание 12


Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 84 единиц?

НАЧАЛО<br/>
    ПОКА нашлось (11111)<br/>
        заменить (222, 1)<br/>
        заменить (111, 2)<br/>
    КОНЕЦ ПОКА<br/>
КОНЕЦ<br/>

```
x = '1'*84
while '11111' in x:
    x = x.replace('222', '1',1)
    x = x.replace('111', '2',1)
print(x)
```

output - 222111
