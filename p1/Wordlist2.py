from itertools import product
#use coustom letters and characters 
value = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$&@#"
for i in range (1,3):
    for j in product(value,repeat=i):
        word = "".join(j)
        p=open("passwordd.text","a")
        p.write(word)
        p.write("\n")
