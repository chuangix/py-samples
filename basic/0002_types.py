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
    return


def showList():
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
