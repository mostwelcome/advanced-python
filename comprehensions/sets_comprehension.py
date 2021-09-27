def main():
    s = "I am trying to remove all the duplicate characters from this and create a set out of it"

    set_comp = {i.upper() for i in s if not i.isspace()}
    print(set_comp)


if __name__ == '__main__':
    main()
