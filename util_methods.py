# demonstrate built-in utility functions


def main():
    # use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]

    #  any will return true if any of the sequence values are true
    print(any(list1))

    #  all will return true only if all values are true
    print(all(list1))

    #  min and max will return minimum and maximum values in a sequence
    print(f'min value in list : {min(list1)}')
    print(f'max value in list : {max(list1)}')

    #  Use sum() to sum up all of the values in a sequence
    print(f'sum value for list: {sum(list1)}')


if __name__ == "__main__":
    main()
