#!/usr/bin/python3
for j in range(0, 10):
    for i in range(0, 10):
        if j == 8 and i == 9:
            print(f"{j}{i}")
        elif j < i:
            print(f"{j}{i}", end=", ")
