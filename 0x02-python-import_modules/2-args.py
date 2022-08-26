#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
argc = len(argv) - 1
if argc < 1:
    print("{} arguments.".format(argc))
else:
    if argc == 1:
        print("{} argument:".format(argc))
    else:
        print("{} arguments:".format(argc))
    for n in range(1, argc + 1):
        print("{}: {}".format(n, argv[n]))