# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a string"
    print(s)

    #  Try combining them.
    # print(b + s)

    #  Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    b1 = b.decode('UTF-8')
    print(b1 + s)

    s1 = s.encode('UTF-8')
    print(s1 + b)
    #  encode the string as UTF-32
    s2 = s.encode('UTF-32')
    print(s2 + b)


if __name__ == "__main__":
    main()
