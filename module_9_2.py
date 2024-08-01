first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# список из длин строк списка first_strings, длина строк не менее 5 символов
first_result = [len(string) for string in first_strings if len(string) >= 5]

#список из пар слов(кортежей) одинаковой длины.
# Каждое слово из списка first_strings должно сравниваться с каждым из second_strings

second_result = [(first, second)
                 for first in first_strings
                 for second in second_strings
                 if len(first) == len(second)]
#В переменную third_result запишите словарь, где парой ключ-значение будет строка-длина строки.
# Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings.
# Условие записи пары в словарь - чётная длина строки.

third_result = {string: len(string)
                for string in first_strings + second_strings
                if len(string) % 2 == 0}


def main():
    print(first_result)
    print(second_result)
    print(third_result)


if __name__ == '__main__':
    main()