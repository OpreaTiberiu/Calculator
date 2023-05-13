import art


def add(first, second):
    return first + second


def substract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    return first / second


def print_ops(ops_dict):
    print(*ops_dict.keys(), sep="\n")
    return input("Pick an operation: ")


print(art.logo)

ops_dict = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

keep_going = True

first_number = float(input("What's the first number?: "))
while keep_going:
    op_sign = print_ops(ops_dict)

    if op_sign not in ops_dict.keys():
        print("ERROR: not a valid operation")
        keep_going = False
    else:
        second_number = float(input("What's the next number?: "))
        result = ops_dict[op_sign](first_number, second_number)

        print(f"{first_number} {op_sign} {second_number} = {result}")

        inp = input("\nWhat's next?\nKeep going from here - Y\nStart from the beginning - C\nExit - Q\n").lower()

        if inp == "q":
            keep_going = False
            print("Byeee")
        elif inp == "c":
            first_number = float(input("What's the first number?: "))
        else:
            first_number = result
