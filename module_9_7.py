'''
Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
'''


def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        prime = 0
        for i in range(2, int(result**0.5) + 1):
            if result % i == 0:
                prime +=1
        if prime:
            print("Составное")
        else:
            print("Простое")
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)


