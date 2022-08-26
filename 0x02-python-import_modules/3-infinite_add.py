#!/usr/bin/python3
if __name__ == "__main__":
    import sys
n = len(sys.argv)
tot = 0
for i in range(1, n):
    tot += int(sys.argv[i])
print(tot)