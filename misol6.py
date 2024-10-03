import random

with open("misol6.txt", "w") as fayl:
    for i in range(20):
        fayl.write(str(random.randint(1, 100)) + " ")  

with open("misol6.txt", "r") as fayl:
    matn = fayl.read().split()  
    for i in matn:
        if int(i) % 2 == 0: 
            print(i,end=" ")