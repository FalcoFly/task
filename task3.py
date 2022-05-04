print("Задание 3.1. Вывести числа от 1 до 100 включительно. Если число делится на 3 то вместо него вывести Foo. Если делится на 5 то вывести Bar. Если делится на 3 и на 5 то вывести FooBar. ")
for i in range(1, 101):
    x = i % 3
    y = i % 5
    if x == 0 and y == 0:
        print("FooBar", end = " ")
    else: 
        if x == 0:
            print("Foo", end = " ")
        elif y == 0:
            print("Bar", end = " ")
        else: print(i, end = " ")
