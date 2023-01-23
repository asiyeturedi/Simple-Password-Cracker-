from random import choice

import time

start_time = time.time()
password_char = [0,1,2,3,4,5,6,7,8,9]
print("password length should be between 4 - 12...")

password_len=int(input("enter the password lenght: "))

while(password_len < 4 or password_len >= 12):
    print("password length should be min 4 max 12")
    password_len =int(input("enter the password lenght: "))

password = " "

fake = " "

steps = 0

for i in range(password_len):
    password += str(choice(password_char))

while True:
    if(password == fake):
        break
    else:
        fake = " "
        for i in range(password_len):
            fake += str(choice(password_char))

            if(len(fake)) != password_len:
                continue
            steps += 1
            print("fake: ",fake,"real:",password,"step:",steps)

finish_time =time.time()
print("password: ", password, "  steps: ", steps, "cracked in " ,finish_time - start_time,  " seconds.")



