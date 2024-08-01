def apply_all_func(int_list, *functions):
    f_dict = {}
    for func in functions:
        f_dict[func.__name__] = func(int_list)
    return f_dict


def main():
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


if __name__ == '__main__':
    main()
