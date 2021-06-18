#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: June DATE, 2021
# This program Welcome! This program creates a data table the size that you
# define. It then fills it with numbers between 10, and 50
# Then it finds the average of these numbers

import random
import consts


# greets the user
def greet():
    print("Welcome! This program creates a data table the size that you")
    print("define. It then fills it with numbers between 10, and 50.")
    print("Then it finds the average of these numbers")


# builds the array
def array_maker(rows, columns):
    done_list = []
    # adds everything into an array and then appends it to the outerlist
    for counter_rows in range(0, rows):
        inner_list = []
        # makes everything into a list
        for counter_columns in range(0, columns):
            num = random.randint(consts.MIN_NUM, consts.MAX_NUM)
            inner_list.append(num)
        # appends the list that was just made to the outer one
        done_list.append(inner_list)
    # returns the list
    return done_list


# displays the list
def list_printer(info, rows):
    total = 0
    average = 0
    num_nums = 0
    for i in info:
        for each in i:
            total = total + each
            num_nums = num_nums + 1
            # stops it from going down a line
            print(each, " ", end='')
        print()
    # calculate the average and then return it
    average = total / num_nums
    return average


def main():
    # get users input
    numRows = input("How many rows do you want: ")
    numColumns = input("How many columns do you want: ")

    # make sure the users num can be an integer
    try:
        # make sure they're all numbers
        numRows = int(numRows)
        numColumns = int(numColumns)
        # call the functions
        main_list = array_maker(numRows, numColumns)
        average = list_printer(main_list, numRows)

        # print the average
        print("Your average is {}".format(average))

    except ValueError:
        print("Not a valid number")


if __name__ == "__main__":
    greet()
    main()
