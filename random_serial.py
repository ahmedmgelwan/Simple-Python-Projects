import string
from random import randint



def genrate_serial(n):
    all_values = string.ascii_letters + string.digits + string.punctuation
    serail = ''
    while n > 0:
        random_index = randint(0, len(all_values) - 1)
        serail += all_values[random_index]
        n -= 1
    return serail


n = int(input('Lenght of Serial: '))

x = genrate_serial(n)
print(x)