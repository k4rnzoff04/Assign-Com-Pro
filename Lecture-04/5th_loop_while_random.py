import random

print("What is my magic number ( 1 to 100 ) ?")
mynumber = random.randint(1, 100)
ntries = 1
yourguess = -1
while ntries < 7 and yourguess != mynumber:
    msg = str(ntries) + ">> "
    if ntries == 6:
        print("Your last chance!")