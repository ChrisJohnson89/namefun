#!/usr/bin/env python3.6

message = input("Enter a message: ")

print("First character:", message[0])
print("Last character:", message[-1])
print("Middle charecter", message[int(len(message) / 2)])

print("Even index characters:", message[0::2])
print("Odd index charecters:", message[1::2])
print("Reversed message:", message[::-1])


