from string import *
from itertools import product
value = ascii_letters + digits + punctuation
#give range for password length
for i in range (8,9):
    for j in product(value,repeat=i):
        word="".join(j)
        p=open("password.txt","a")
        p.write(word)
        p.write("\n")
