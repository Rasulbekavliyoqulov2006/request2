import json

with open("misol9.json", "r") as fayl:
    malumot = json.load(fayl)
    

yosh = [foydalanuvchi["yosh"] for foydalanuvchi in malumot]

maxx = max(yosh)
min = min(yosh)

print(f"eng katta yosh: {maxx}")
print(f"eng kichik yosh: {min}")