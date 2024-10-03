import json

 
with open("misol9.json", "r") as fayl:
    foydalanuvchilar = json.load(fayl)

 
yosh_18 = [foydalanuvchi for foydalanuvchi in foydalanuvchilar if foydalanuvchi["yosh"] >= 18]


for i in yosh_18:
    print(f"Ism: {i['ism']},  Familiya: {i['familiya']},  Yosh: {i['yosh']}")
