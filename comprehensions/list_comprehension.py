def main():

    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15]

    even_squared = [k**2 for k in evens]
    print(even_squared)

    odds_squared = [k**2 for k in odds if k > 3 and k < 10]
    print(odds_squared)


if __name__ == '__main__':
    main()
