# use iterator functions like enumerate, zip, iter, next

def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # use iter to create an iterator over a collection
    daysitr = iter(days)
    print(next(daysitr))

    # iterate using a function and a sentinel
    with open('testfile.txt', 'r') as fp:
        # sentinel value when iterator will stop
        for line in iter(fp.readline, ''):
            print(line)

    #  use regular interation over the days
    for m in range(len(days)):
        print(m, days[m])

    #  using enumerate reduces code and provides a counter
    for i, m in enumerate(days, start=1):
        print(i, m)

    #  use zip to combine sequences
    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], m[1])


if __name__ == "__main__":
    main()
