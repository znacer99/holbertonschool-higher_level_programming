#!/usr/bin/python3
def uppercase(str):
    for j in range(len(str)):
        word = ord(str[j])
        if (word >= 97 and word <= 122):
            word = word - 32
        print("{:c}".format(word), end="")
print()
