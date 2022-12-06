import random
print('hello, Welcome to Password generator!')

length = int(input('Enter the length of password: '))

lower =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
        'z')
upper =('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
      'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
     'Z')
num = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
symbols =('@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<')
all = lower + upper + num + symbols
sai = random.sample(all,length)
password = "".join(sai)
if length>=12:
    print("Your Password is: ",password)
else:
    print("Not Possible")
