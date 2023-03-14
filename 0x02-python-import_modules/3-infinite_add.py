#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argsSum = 0
    argsLen = len(argv) - 1

    if argsLen >= 1:
        for args in range(1, argsLen + 1):
            argsSum += int(argv[args])
        print("{}".format(argsSum))
