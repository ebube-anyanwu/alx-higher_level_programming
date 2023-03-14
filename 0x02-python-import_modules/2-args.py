#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    args_len = len(argv) - 1
    if args_len == 0:
        print("0 arguments.")
    elif args_len == 1:
        print("{} argument:\n{}: {}".format(args_len, args_len, argv[1]))
    else:
        print("{} arguments:".format(args_len))
        for args in range(1, args_len + 1):
            print("{}: {}".format(args, argv[args]))
