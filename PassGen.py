import random
import string

msg = 'Welcome to PassGen'
passWord = ''
temp = ''

print(msg)

print('How many characters do you need your password to be?')

num_chars = int(input())

print('Does your password need to contain special characters? (y/n)')

special_chars = input().lower()

if special_chars == 'y':
    for i in range(num_chars):
        temp = random.choice(string.ascii_letters + string.digits + string.punctuation)
        passWord = passWord+temp
    print(passWord)

elif special_chars == 'n':
    for i in range(num_chars):
        temp = random.choice(string.ascii_letters + string.digits)
        passWord = passWord+temp
    print(passWord)
    #test