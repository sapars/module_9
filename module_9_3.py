first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# first_result  высчитывает разницу длин строк из списков first и second, если их длины не равны.
#  Для перебора строк попарно из двух списков используйте функцию zip.
first_result = (len(first_string) - len(second_string)
                for first_string, second_string in zip(first, second)
                if len(first_string) != len(second_string))

# second_result  содержит результаты сравнения строк в одинаковых позициях из списков first и second.
# Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.
second_result = (len(first[i]) == len(second[i])
                 for i in range(min(len(first), len(second))))


def main():
    print(list(first_result))
    print(list(second_result))


if __name__ == '__main__':
    main()