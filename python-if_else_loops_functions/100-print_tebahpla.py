#!/usr/bin/python3
index = 0
for letter in range(122, 96, -1):
    if index % 2 == 0:
        print("{}".format(chr(letter)), end="")
    else:
        print("{}".format(chr(letter - 32)), end="")
    index += 1
