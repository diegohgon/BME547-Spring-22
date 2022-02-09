def function_name():
    b = 2
    c = 3
    a = b + c
    return a


def main():
    try:
        a = function_name()
        print(a)
    except NameError:
        print("Value not found")


if __name__ == "__main__":
    main()
