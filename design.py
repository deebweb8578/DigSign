import math
import random
import os
import time

os.system('clear')
print(
    "* *\n *  *\n  *    *\n   *      *\n    *        *\n     *          *\n      *            *\n       *              *\n        *                *\n         *                  *\n          *                    *\n           * * * * * * * * * * * * \n                  \033[91mMade by:  \033[93mRIFAT")

print(" ")
print(" ")
time.sleep(1)
print("\033[95mLoading.....")
time.sleep(2)
os.system('clear')
spaces = 40
word = int(input("\033[96m[?] How many word in your line? \033[91m(Example: In the line 'I love You' has '3' word. And for this enter '3'. And Word no.1=I, Word no.2=Love and so on.) \033[93m:"))
print(" ")
text = []
for i in range(word):
    text.append(input('\033[96mEnter word no. ' + str(i+1) + ':\033[93m'))
print(" ")


def sine():
    for angle in range(0, 360, 10):
        space = int((spaces / 2) * math.sin(math.radians(angle)))
        serial = int((angle/10) % len(text))
        print((int(spaces / 2) + space) * ' ' + text[serial])


def v():
    for i in range(12):
        serial = int(i % len(text))
        print(i * ' ' + text[serial] + i * '  ' + text[serial])
    for j in range(11, -1, -1):
        serial = int(j % len(text))
        print(j * ' ' + text[serial] + j * '  ' + text[serial])


def sincos():
    for angle in range(0, 180, 10):
        space1 = int((spaces / 2) * math.sin(math.radians(angle + 180)))
        space2 = int((spaces / 2) * math.sin(math.radians(angle)))
        serial = int((angle/10) % len(text))
        print((int(spaces / 2) + space1) * ' ' + text[serial] + ((int(spaces / 2)) - 15 - space1 + space2) * ' ' + text[serial])


def randoms():
    choice = random.randint(1, 3)
    if choice == 1:
        sine()
    if choice == 2:
        v()
    if choice == 3:
        sincos()


choices = input('\033[96mWhat type? \n\033[91m[s] Sine shape (Look ike a snake)\n[sc] Sine Cosine shape (Look like a snake and a reverse) \n[v] V shape (Look like "V")\n[r] Random (Randomize previous shapes)\n \033[93m\n[?] ')
print(" ")
num = int(input("\033[96m[?] How much? \033[91m(Enter a number like '10' or anything. Higher number give a long output) \033[93m"))
os.system('clear')
for i in range(num):
    if choices == 'r':
        randoms()
    if choices == 's':
        sine()
    if choices == 'sc':
        sincos()
    if choices == 'v':
        v()
