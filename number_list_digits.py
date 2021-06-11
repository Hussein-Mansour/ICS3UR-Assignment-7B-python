#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Wed/Jun9/2021
# this program takes a number and returns a list of its digits


def new_list(int_list):
    # this function return list of its digits
    lst = int_list[0]
    # process
    process = list(map(int, str(lst)))
    # return
    return process


def main():
    # this function uses a 2D list
    List_of_numbers = []

    # start
    print("Starting ...")
    print("\n")
    # input & output
    try:
        input_from_user = int(input("The original number is: "))
        List_of_numbers.append(input_from_user)

        print_list = new_list(List_of_numbers)

        print(
            "\n\nThe list from number is : {0}"
            .format(print_list))
    except Exception:
        print("\nInvalid Input!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
