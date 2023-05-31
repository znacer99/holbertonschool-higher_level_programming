#!/usr/bin/python3
def uppercase(str):
    for j in range(len(str)):
        klma = ord(str[j])
        if (klma >= 97 and klma <= 122):
            klma = klma - 32
        print("{:c}".format(klma), end="")
print()
