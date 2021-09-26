# use transform functions like sorted, filter, map


def filter_func(x):
    return x % 2 != 0


def filter_func2(x):
    return x.islower()


def square_func(x):
    return x ** 2


def to_grade(x):
    if x >= 90:
        return 'A'
    if x >= 80:
        return 'B'
    if x >= 70:
        return 'C'
    if x >= 50:
        return 'D'
    else:
        return 'F'


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    #  use filter to remove items from a list
    odds = list(filter(filter_func, nums))
    print(odds)

    #  use filter on non-numeric sequence
    lower_case = list(filter(filter_func2, chars))
    print(lower_case)
    #  use map to create a new sequence of values
    squares = list(map(square_func, nums))
    print(squares)

    #  use sorted and map to change numbers to grades
    # grades = sorted(grades)
    result = list(map(to_grade, grades))
    print(result)


if __name__ == "__main__":
    main()
