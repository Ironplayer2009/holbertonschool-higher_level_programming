#!/usr/bin/python3
def uppercase(str):
    for new_char in str:
        if 97 <= ord(new_char) <= 122:
            new_char = chr(ord(new_char) - 32)
        print("{}".format(new_char), end="")
