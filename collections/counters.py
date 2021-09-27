from collections import Counter


def main():

    # list of students in class 1
    class1 = ['a', 'b', 'c', 'a', 'b']

    # list of students in class 2
    class2 = ['d', 'e', 'f', 'a', 'b']

    # create a counter for class1 and class2

    c1 = Counter(class1)
    c2 = Counter(class2)

    # how many student in class1 named 'a'?
    print(c1['a'])

    # how many students are in class 1?
    print(sum(c1.values()), 'Students in class 1')
    # Combine the two classes

    c1.update(c2)
    print(sum(c1.values()), 'Students in class 1')

    # most common name in two classes

    print(c1.most_common(3))

    # separate classes again
    c1.subtract(c2)
    print(sum(c1.values()), 'Students in class 1')

    # what items are present in both the counters
    print(c1 & c2)


if __name__ == '__main__':
    main()
