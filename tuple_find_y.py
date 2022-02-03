def interface():
    keep_running = True
    while keep_running:
        print("Options:")
        print("1-Enter x1")
        print("2-Enter y1")
        print("3-Enter x2")
        print("4-Enter y2")
        print("5-Enter x3")
        print("6-Calculate y3")
        print("9-Quit")
        choice = input("Enter your choice: ")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            input_x1 = x1_driver()
        elif choice == "2":
            input_y1 = y1_driver()
        elif choice == "3":
            input_x2 = x2_driver()
        elif choice == "4":
            input_y2 = y2_driver()
        elif choice == "5":
            input_x3 = x3_driver()
        elif choice == "6":
            expected_y3 = check_y_value(
                input_x1, input_x2, input_x3, input_y1, input_y2)
    return


def accept_input(test_name):
    entry = input("Enter the {} value: ".format(test_name))
    return int(entry)


def x1_driver():
    input_x1 = accept_input("x1")
    return input_x1


def x2_driver():
    input_x2 = accept_input("x2")
    return input_x2


def x3_driver():
    input_x3 = accept_input("x3")
    return input_x3


def y1_driver():
    input_y1 = accept_input("y1")
    return input_y1


def y2_driver():
    input_y2 = accept_input("y2")
    return input_y2


def check_y_value(input_x1, input_x2, input_x3, input_y1, input_y2):
    m = (input_y2 - input_y1)/(input_x2 - input_x1)
    y_intercept = input_y1 - m * input_x1

    expected_y3 = input_x3 * m + y_intercept
    print("The expected y3 value is {}.".format(expected_y3))
    return expected_y3


if __name__ == "__main__":
    interface()
