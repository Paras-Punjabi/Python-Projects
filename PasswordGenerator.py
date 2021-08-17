import random

lowerAlpha = "abcdefghijklmnopqrstuvwxyz"
upperAlpha = lowerAlpha.upper()
specialCharacters = "?/><.,:;][{\|=+-_)(*&^%$#@!~`"
numbers = "1234567890"

n = int(input("Enter the length of your password\n"))

if(n <= len(lowerAlpha) + len(upperAlpha) + len(specialCharacters)+ len(numbers)):
    all = lowerAlpha + upperAlpha + specialCharacters + numbers
    array = list(all)
    random.shuffle(array)
    password = []
    for i in range(0,n):
        password.append(array[i])

    password = "".join(password)
    print(f"Your Random password is {password}")

else:
    print("Password length is too big")


