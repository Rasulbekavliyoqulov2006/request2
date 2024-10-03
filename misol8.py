import json

with open("misol7.json", "r") as fayl:
    malumot = json.load(fayl)
malumot["manzil"] = {
    "shahar": input("shaharingizni kiriting: "),
    "kocha": input("kocha nomini kiriting: "),
    "uy": int(input("uy raqamingizni kiriting: "))
}

with open("misol8.json", "w") as fayl:
    json.dump(malumot, fayl, indent=4)