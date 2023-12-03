import sys

REQUIRED_MAJOR_VERSION = 3
if sys.version_info.major < REQUIRED_MAJOR_VERSION:
    sys.exit(
        "Current version %s.%s.%s is not satisfied to %s.x.x"
        % (
            sys.version_info.major,
            sys.version_info.minor,
            sys.version_info.micro,
            REQUIRED_MAJOR_VERSION,
        )
    )


def showNumber():
    print(sys._getframe().f_code.co_name)
    a, b, c, d = 20, 5.5, True, 4 + 3j
    print("The type of", a, "is", type(a))
    print("The type of", b, "is", type(b))
    print("The type of", c, "is", type(c))
    print("The type of", d, "is", type(d))
    print('is "bool" a subclass of "int"?', issubclass(bool, int))
    return


def showString():
    s = "Python"
    print(s)
    print(s[0:-1])
    print(s[0])
    print(s[2:5])
    print(s[2:])
    print(s * 2)
    print(s + " is nice")
    print("Python\n is nice")
    print(r"Python\n is nice")
    return


def showList():  # TODO Split this function into several sub-functions
    l1 = ["abcd", 786, 2.23, "Python", 70.2]
    l2 = [123, "Python"]
    print(l1)
    print(l1[0])
    print(l1[1:3])
    print(l1[2:])
    print(l2 * 2)
    print(l1 + l2)
    l3 = [1, 2, 3, 4, 5, 6]
    print(l3)
    print(l3[0:6])
    print(l3[0:5])
    print(l3[0:-1])
    print(l3[0:5:2])
    print(l3[0:])
    print(l3[0::2])
    l3[0] = 9
    l3[2:5] = [13, 14, 15]
    print(l3)
    l3[2:5] = []
    print(l3)
    return


def showTuple():
    return


def showSet():
    return


def showDictionary():
    return


showNumber()
showString()
showList()
showTuple()
showSet()
showDictionary()
